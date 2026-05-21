from pathlib import Path

import numpy as np
import tensorflow as tf

from transformer_tts.utils.training_config_manager import TrainingConfigManager
from transformer_tts.data.text.tokenizer import Tokenizer
from transformer_tts.data.metadata_readers import DataReader, DataKind


class Dataset:
    def __init__(self,
                 mel_channels: int,
                 tokenizer: Tokenizer,
                 data_reader: DataReader,
                 mel_directory: Path,
                 duration_directory: Path,
                 pitch_per_char_directory: Path,
                 bucket_boundaries: list,
                 bucket_batch_sizes: list,
                 seed: None | int = None,
                 shuffle=True, **_):
        self.metadata_reader = data_reader
        self.tokenizer = tokenizer
        self.mel_directory = Path(mel_directory)
        self.duration_directory = Path(duration_directory)
        self.pitch_per_char_directory = Path(pitch_per_char_directory)
        self.zfill = self.tokenizer.zfill

        self.output_types = (tf.float32, tf.int32, tf.int32,
                             tf.float32, tf.int32, tf.int32)
        self.padded_shapes = ([None, mel_channels], [None],
                              [None], [None], [], [])
        
        samples = self.metadata_reader.filenames[:]
        dataset = tf.data.Dataset.from_tensor_slices(samples)
        if shuffle:
            dataset = dataset.shuffle(
                buffer_size=len(samples),
                seed=seed,
                reshuffle_each_iteration=False
            )

        dataset = dataset.map(self._tf_process_sample,
                              num_parallel_calls=tf.data.AUTOTUNE)

        binned_data = dataset.bucket_by_sequence_length(
            self.get_mel_length,
            bucket_boundaries=bucket_boundaries,
            bucket_batch_sizes=bucket_batch_sizes,
            padded_shapes=self.padded_shapes # type: ignore
        )
        self.dataset = binned_data
        self.data_iter = iter(binned_data.repeat(-1))

    def next_batch(self):
        return next(self.data_iter)

    def all_batches(self):
        return iter(self.dataset)


    def process_sample(self, sample_name: str):
        text, speaker_id, language_id = self.metadata_reader.text_dict[sample_name]
        mel = np.load(
            (self.mel_directory / sample_name).with_suffix('.npy').as_posix())
        durations = np.pad(np.load(
            (self.duration_directory / sample_name).with_suffix('.npy').as_posix()), (self.zfill, 0))
        pitch = np.pad(np.load((self.pitch_per_char_directory / sample_name).with_suffix('.npy').as_posix()),
                       (self.zfill, 0))

        encoded_phonemes = self.tokenizer(text, speaker_id=speaker_id)
        return mel, encoded_phonemes, durations, pitch, speaker_id, language_id
    
    def _process_sample_py(self, sample_name: tf.Tensor):
        # Convert tf.string -> Python str, then run Python-side preprocessing.
        return self.process_sample(sample_name.numpy().decode('utf-8')) # type: ignore
    
    def _tf_process_sample(self, sample_name: tf.Tensor):
        outputs = tf.py_function(func=self._process_sample_py,
                                 inp=[sample_name],
                                 Tout=self.output_types)
        # Set static shapes to help downstream padding/bucketing
        for tensor, shape, dtype in zip(outputs, self.padded_shapes, self.output_types):
            tensor = tf.cast(tensor, dtype)
            tensor.set_shape(shape)
        return tuple(outputs)

    @staticmethod
    def get_mel_length(mel, *_) -> tf.Tensor:
        return tf.shape(mel)[0]

    @classmethod
    def from_config(cls,
                    config: TrainingConfigManager,
                    tokenizer: Tokenizer,
                    kind: str,
                    bucket_boundaries: list,
                    bucket_batch_sizes: list,
                    **kwargs):
        kind = DataKind(kind)
        metadata_reader = DataReader.from_config(config,
                                                 kind=kind)
        return cls(mel_channels=config.config['mel_channels'],
                   tokenizer=tokenizer,
                   data_reader=metadata_reader,
                   mel_directory=config.mel_dir,
                   duration_directory=config.duration_dir,
                   pitch_per_char_directory=config.pitch_per_char,
                   seed=config.seed,
                   bucket_boundaries=bucket_boundaries,
                   bucket_batch_sizes=bucket_batch_sizes,
                   **kwargs)