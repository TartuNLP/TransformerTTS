import logging
from enum import Enum
from typing import Any

import tensorflow as tf
import keras
import numpy as np


from transformer_tts.model.layers import StatPredictor, Expand, SelfAttentionBlocks
from transformer_tts.model.transformer_utils import (
    create_encoder_padding_mask,
    create_mel_padding_mask,
)
from transformer_tts.model.losses import weighted_sum_losses, masked_mean_absolute_error
from transformer_tts.data.text import TextToTokens

logger = logging.getLogger(__name__)


class Multispeaker(str, Enum):
    GST = "GST"
    embedding = "embedding"

@keras.saving.register_keras_serializable()
class ForwardTransformer(tf.keras.models.Model):
    optimizer: tf.keras.optimizers.Optimizer = None

    def __init__(
        self,
        encoder_model_dimension: int,
        decoder_model_dimension: int,
        dropout_rate: float,
        decoder_num_heads: list,
        encoder_num_heads: list,
        encoder_max_position_encoding: int,
        decoder_max_position_encoding: int,
        encoder_dense_blocks: int,
        decoder_dense_blocks: int,
        duration_conv_filters: list,
        pitch_conv_filters: list,
        duration_kernel_size: int,
        pitch_kernel_size: int,
        predictors_dropout: float,
        mel_channels: int,
        alphabet: str,
        transposed_attn_convs: bool,
        encoder_attention_conv_filters: list | None = None,
        decoder_attention_conv_filters: list | None = None,
        encoder_attention_conv_kernel: int | None = None,
        decoder_attention_conv_kernel: int | None = None,
        encoder_feed_forward_dimension: int | None = None,
        decoder_feed_forward_dimension: int | None = None,
        use_layernorm: bool = False,
        multispeaker: str | None = None,
        n_speakers: int = 1,
        n_languages: int = 1,
        **kwargs,
    ):
        super(ForwardTransformer, self).__init__()
        self.config = self._make_config(locals(), kwargs)
        self.multispeaker = (
            Multispeaker(multispeaker) if multispeaker is not None else None
        )
        self.n_speakers = n_speakers
        self.n_languages = n_languages
        self.text_pipeline = TextToTokens.default(
            alphabet=alphabet,
            gst=(self.multispeaker == Multispeaker.GST),
            zfill=len(str(int(n_speakers - 1))),
        )
        self.symbols = self.text_pipeline.tokenizer.alphabet
        self.encoder_prenet = tf.keras.layers.Embedding(
            self.text_pipeline.tokenizer.vocab_size,
            encoder_model_dimension,
            name="Embedding",
        )
        self.encoder = SelfAttentionBlocks(
            model_dim=encoder_model_dimension,
            dropout_rate=dropout_rate,
            num_heads=encoder_num_heads,
            feed_forward_dimension=encoder_feed_forward_dimension,
            maximum_position_encoding=encoder_max_position_encoding,
            dense_blocks=encoder_dense_blocks,
            conv_filters=encoder_attention_conv_filters,
            kernel_size=encoder_attention_conv_kernel,
            conv_activation="relu",
            transposed_convs=transposed_attn_convs,
            use_layernorm=use_layernorm,
            name="Encoder",
        )
        if self.multispeaker == Multispeaker.embedding:
            self.speaker_embedder = tf.keras.layers.Embedding(
                self.n_speakers, encoder_model_dimension, name="speaker_embedder"
            )
        else:
            self.speaker_embedder = None

        if self.n_languages > 1:
            assert self.multispeaker == Multispeaker.embedding, (
                "Multilingual models must use multispeaker embedding"
            )
            self.language_embedder = tf.keras.layers.Embedding(
                self.n_languages, encoder_model_dimension, name="language_embedder"
            )
        else:
            self.language_embedder = None

        self.dur_pred = StatPredictor(
            conv_filters=duration_conv_filters,
            kernel_size=duration_kernel_size,
            conv_padding="same",
            conv_activation="relu",
            dense_activation="relu",
            dropout_rate=predictors_dropout,
            name="dur_pred",
        )
        self.expand = Expand(name="expand", model_dim=encoder_model_dimension)
        self.pitch_pred = StatPredictor(
            conv_filters=pitch_conv_filters,
            kernel_size=pitch_kernel_size,
            conv_padding="same",
            conv_activation="relu",
            dense_activation="linear",
            dropout_rate=predictors_dropout,
            name="pitch_pred",
        )
        self.pitch_embed = tf.keras.layers.Dense(
            encoder_model_dimension, activation="relu"
        )
        self.decoder = SelfAttentionBlocks(
            model_dim=decoder_model_dimension,
            dropout_rate=dropout_rate,
            num_heads=decoder_num_heads,
            feed_forward_dimension=decoder_feed_forward_dimension,
            maximum_position_encoding=decoder_max_position_encoding,
            dense_blocks=decoder_dense_blocks,
            conv_filters=decoder_attention_conv_filters,
            kernel_size=decoder_attention_conv_kernel,
            conv_activation="relu",
            transposed_convs=transposed_attn_convs,
            use_layernorm=use_layernorm,
            name="Decoder",
        )
        self.out = tf.keras.layers.Dense(mel_channels)

        self.training_input_signature = [
            tf.TensorSpec(shape=(None, None), dtype=tf.int32),
            tf.TensorSpec(shape=(None,), dtype=tf.int32),
            tf.TensorSpec(shape=(None,), dtype=tf.int32),
            tf.TensorSpec(shape=(None, None, mel_channels), dtype=tf.float32),
            tf.TensorSpec(shape=(None, None), dtype=tf.int32),
            tf.TensorSpec(shape=(None, None), dtype=tf.float32),
        ]

        tf.function(func=self.train_step, input_signature=self.training_input_signature)
        tf.function(func=self.val_step, input_signature=self.training_input_signature)

        self.loss_functions = [
            masked_mean_absolute_error,
            masked_mean_absolute_error,
            masked_mean_absolute_error,
        ]
        self.loss_weights = [1.0, 1.0, 3.0]

    @property
    def step(self):
        return int(self.optimizer.iterations)

    @property
    def step_tf(self):
        return self.optimizer.iterations
    
    def get_config(self) -> dict[str, Any]:
        config = super().get_config()
        config.update(self.config)
        return config

    def build(self, input_shape):
        super().build(input_shape)
        self.build_model_weights()

    def _step(
        self,
        input_sequence,
        speaker_id,
        language_id,
        target_sequence,
        target_durations,
        target_pitch,
        training: bool = False
    ):
        target_durations = tf.expand_dims(target_durations, -1)
        target_pitch = tf.expand_dims(target_pitch, -1)
        mel_len = int(tf.shape(target_sequence)[1])
        model_out = self(
            input_sequence,
            speaker_id=speaker_id,
            language_id=language_id,
            target_durations=target_durations,
            target_pitch=target_pitch,
            training=training,
        )
        loss, loss_vals = weighted_sum_losses(
            (target_sequence, target_durations, target_pitch),
            (
                model_out["mel"][:, :mel_len, :],
                model_out["duration"],
                model_out["pitch"],
            ),
            self.loss_functions,
            self.loss_weights,
        )
        model_out.update({"loss": loss})
        model_out.update(
            {
                "losses": {
                    "mel": loss_vals[0],
                    "duration": loss_vals[1],
                    "pitch": loss_vals[2],
                }
            }
        )
        return model_out, loss

    def train_step(self, *args, **kwargs):
        with tf.GradientTape() as tape:
            model_out, loss = self._step(*args, training=True, **kwargs)

        gradients = tape.gradient(loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))
        return model_out

    def val_step(self, *args, **kwargs):
        model_out, _ = self._step(*args, training=False, **kwargs)
        return model_out

    def predict(
        self,
        inp,
        encode=True,
        speed_regulator=1.0,
        phoneme_max_duration=None,
        phoneme_min_duration=None,
        max_durations_mask=None,
        min_durations_mask=None,
        phoneme_durations=None,
        phoneme_pitch=None,
        speaker_id: int | list[int] = 0,
        language_id: int | list[int] = 0,
    ):
        if encode:
            inp = self.text_pipeline(inp, speaker_id=speaker_id)
        expand = len(tf.shape(inp)) == 1
        if expand:
            inp = tf.expand_dims(inp, 0)
        inp = tf.cast(inp, tf.int32)
        duration_scalar = tf.cast(1.0 / speed_regulator, tf.float32)
        max_durations_mask = self._make_max_duration_mask(inp, phoneme_max_duration)
        min_durations_mask = self._make_min_duration_mask(inp, phoneme_min_duration)

        speaker_id = tf.convert_to_tensor(speaker_id, dtype=tf.int32)  # type: ignore
        language_id = tf.convert_to_tensor(language_id, dtype=tf.int32)  # type: ignore

        out = self.call(
            inp,
            target_durations=phoneme_durations,
            target_pitch=phoneme_pitch,
            training=False,
            durations_scalar=duration_scalar,
            max_durations_mask=max_durations_mask,
            min_durations_mask=min_durations_mask,
            speaker_id=speaker_id,
            language_id=language_id,
        )
        if expand:
            out["mel"] = tf.squeeze(out["mel"])
            out["pitch"] = tf.squeeze(out["pitch"])
            out["duration"] = tf.squeeze(out["duration"])
        return out

    def call(
        self,
        x,
        speaker_id,
        language_id,
        target_durations=None,
        target_pitch=None,
        durations_scalar: float | tf.Tensor = 1.0,
        max_durations_mask=None,
        min_durations_mask=None,
        training=False,
    ):
        encoder_padding_mask = create_encoder_padding_mask(x)
        x = self.encoder_prenet(x)

        if self.language_embedder is not None:
            language_emb = self.language_embedder(language_id)
            if len(x.shape) == 3:
                language_emb = tf.expand_dims(language_emb, axis=1)
            x = x + language_emb

        x, encoder_attention = self.encoder(
            x, training=training, mask=encoder_padding_mask
        )
        padding_mask = 1.0 - tf.squeeze(encoder_padding_mask, axis=(1, 2))[:, :, None]

        if self.speaker_embedder is not None:
            speaker_emb = self.speaker_embedder(speaker_id)
            if len(x.shape) == 3:
                speaker_emb = tf.expand_dims(speaker_emb, axis=1)

            durations = self.dur_pred(
                x + speaker_emb, training=training, mask=padding_mask
            )
            pitch = self.pitch_pred(
                x + speaker_emb, training=training, mask=padding_mask
            )
        else:
            speaker_emb = None
            durations = self.dur_pred(x, training=training, mask=padding_mask)
            pitch = self.pitch_pred(x, training=training, mask=padding_mask)

        if target_pitch is not None:
            pitch_embed = self.pitch_embed(target_pitch)
        else:
            pitch_embed = self.pitch_embed(pitch)
        x = x + pitch_embed
        if target_durations is not None:
            use_durations = target_durations
        else:
            use_durations = durations * durations_scalar
        if max_durations_mask is not None:
            use_durations = tf.math.minimum(
                use_durations, tf.expand_dims(max_durations_mask, -1)
            )
        if min_durations_mask is not None:
            use_durations = tf.math.maximum(
                use_durations, tf.expand_dims(min_durations_mask, -1)
            )
        mels = self.expand(x, use_durations)
        if self.speaker_embedder is not None:
            mels = tf.concat((speaker_emb, mels), 1)
        expanded_mask = create_mel_padding_mask(mels)
        mels, decoder_attention = self.decoder(
            mels, training=training, mask=expanded_mask, reduction_factor=1
        )
        if self.speaker_embedder is not None:
            mels = mels[:, 1:, :]
        mels = self.out(mels)
        model_out = {
            "mel": mels,
            "duration": durations,
            "pitch": pitch,
            "expanded_mask": expanded_mask,
            "encoder_attention": encoder_attention,
            "decoder_attention": decoder_attention,
        }
        return model_out

    def _make_max_duration_mask(self, encoded_text, phoneme_max_duration):
        np_text = np.array(encoded_text)
        new_mask = np.ones(tf.shape(encoded_text)) * float("inf")
        if phoneme_max_duration is not None:
            for item in phoneme_max_duration.items():
                phon_idx = self.text_pipeline.tokenizer(item[0])[0]
                new_mask[np_text == phon_idx] = item[1]
        return tf.cast(tf.convert_to_tensor(new_mask), tf.float32)

    def _make_min_duration_mask(self, encoded_text, phoneme_min_duration):
        np_text = np.array(encoded_text)
        new_mask = np.zeros(tf.shape(encoded_text))
        if phoneme_min_duration is not None:
            for item in phoneme_min_duration.items():
                phon_idx = self.text_pipeline.tokenizer(item[0])[0]
                new_mask[np_text == phon_idx] = item[1]
        return tf.cast(tf.convert_to_tensor(new_mask), tf.float32)

    def set_constants(self, learning_rate: float | None = None, **_):
        if learning_rate is not None:
            self.optimizer.learning_rate.assign(float(learning_rate))

    def compile_model(self, optimizer):
        self.compile(
            loss=self.loss_functions,
            loss_weights=self.loss_weights,
            optimizer=optimizer,
        )
        self.build_model_weights()

    def build_model_weights(self) -> None:
        self.call(
            tf.zeros((1, 1)),
            target_durations=tf.ones((1, 1, 1)),
            speaker_id=tf.zeros(
                1,
            ),
            language_id=tf.zeros(
                1,
            ),
            training=False,
        )
        if hasattr(self, "optimizer") and self.optimizer is not None:
            self.optimizer.build(self.trainable_variables)

        logger.debug(self.summary())

    @staticmethod
    def _make_config(locals_: dict, kwargs: dict) -> dict:
        config = {}
        keys = [
            k
            for k in locals_.keys()
            if (k not in kwargs) and (k not in ["self", "__class__", "kwargs"])
        ]
        for k in keys:
            if isinstance(locals_[k], dict):
                config.update(locals_[k])
            else:
                config.update({k: locals_[k]})
        config.update(kwargs)
        return config

    @classmethod
    def from_config(cls, config: dict):
        return cls(**config)
