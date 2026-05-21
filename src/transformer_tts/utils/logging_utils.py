from pathlib import Path

import tensorflow as tf


from transformer_tts.utils.display import tight_grid, buffer_image, plot_image, plot_1d
from transformer_tts.data.audio import Audio
from transformer_tts.model.vec_ops import norm_tensor


def control_frequency(f):
    def apply_func(*args, **kwargs):
        # args[0] is self
        plot_all = ("plot_all" in kwargs) and kwargs["plot_all"]
        if (args[0].step % args[0].plot_frequency == 0) or plot_all:
            result = f(*args, **kwargs)
            return result
        else:
            return None

    return apply_func


class SummaryManager:
    _audio: Audio
    """Writes tensorboard logs during training.

    :arg model: model object that is trained
    :arg log_dir: base directory where logs of a config are created
    :arg config: configuration dictionary
    :arg max_plot_frequency: every how many steps to plot
    """

    def __init__(
        self,
        model: None | tf.keras.models.Model,
        log_dir: str | Path,
        config: dict,
        max_plot_frequency=10,
        default_writer="log_dir",
    ):
        self.model = model
        self.log_dir = Path(log_dir)
        self.config = config
        self._audio = Audio.from_config(config)
        self.plot_frequency = max_plot_frequency
        self.default_writer = default_writer
        self.writers = {}
        self.add_writer(tag=default_writer, path=self.log_dir, default=True)

    @property
    def step(self):
        if self.model is not None:
            return self.model.step
        else:
            return 0

    def add_writer(self, path, tag=None, default=False):
        """Adds a writer if the writer does not exist already.
        To avoid spamming writers on disk.

        returns the writer on path with tag or path
        """
        if not tag:
            tag = path
        if tag not in self.writers.keys():
            self.writers[tag] = tf.summary.create_file_writer(str(path))
        if default:
            self.default_writer = tag
        return self.writers[tag]

    def add_scalars(self, tag, dictionary):
        for k in dictionary.keys():
            with self.add_writer(str(self.log_dir / k)).as_default():
                tf.summary.scalar(name=tag, data=dictionary[k], step=self.step)

    def add_scalar(self, tag, scalar_value):
        with self.writers[self.default_writer].as_default():
            tf.summary.scalar(name=tag, data=scalar_value, step=self.step)

    def add_image(self, tag, image):
        with self.writers[self.default_writer].as_default():
            tf.summary.image(name=tag, data=image, step=self.step, max_outputs=4)

    def add_histogram(self, tag, values, buckets=None):
        with self.writers[self.default_writer].as_default():
            tf.summary.histogram(name=tag, data=values, step=self.step, buckets=buckets)

    def add_audio(self, tag, wav, sr=None, description=None):
        if sr is None:
            sr = self.config["sampling_rate"]
        with self.writers[self.default_writer].as_default():
            tf.summary.audio(
                name=tag,
                data=wav,
                sample_rate=sr,
                step=self.step,
                description=description,
            )

    def add_text(self, tag, text):
        with self.writers[self.default_writer].as_default():
            tf.summary.text(name=tag, data=text, step=self.step)

    def attention_heads(self, outputs: dict, tag="", fname: list | None = None):
        for layer in ["encoder_attention", "decoder_attention"]:
            for k in outputs[layer].keys():
                if fname is None:
                    image = tight_grid(
                        norm_tensor(outputs[layer][k][0])
                    )  # dim 0 of image_batch is now number of heads
                    if k == "Decoder_LastBlock_CrossAttention":
                        batch_plot_path = f"{tag}_Decoder_Final_Attention"
                    else:
                        batch_plot_path = f"{tag}_{layer}/{k}"
                    self.add_image(
                        str(batch_plot_path),
                        tf.expand_dims(tf.expand_dims(image, 0), -1),
                    )
                else:
                    for j, file in enumerate(fname):
                        image = tight_grid(
                            norm_tensor(outputs[layer][k][j])
                        )  # dim 0 of image_batch is now number of heads
                        if k == "Decoder_LastBlock_CrossAttention":
                            batch_plot_path = f"{tag}_Decoder_Final_Attention/{file.numpy().decode('utf-8')}"
                        else:
                            batch_plot_path = (
                                f"{tag}_{layer}/{k}/{file.numpy().decode('utf-8')}"
                            )
                        self.add_image(
                            str(batch_plot_path),
                            tf.expand_dims(tf.expand_dims(image, 0), -1),
                        )

    def last_attention(self, outputs, tag="", fname=None):
        if fname is None:
            image = tight_grid(
                norm_tensor(
                    outputs["decoder_attention"]["Decoder_LastBlock_CrossAttention"][0]
                )
            )  # dim 0 of image_batch is now number of heads
            batch_plot_path = f"{tag}_Decoder_Final_Attention"
            self.add_image(
                str(batch_plot_path), tf.expand_dims(tf.expand_dims(image, 0), -1)
            )
        else:
            for j, file in enumerate(fname):
                image = tight_grid(
                    norm_tensor(
                        outputs["decoder_attention"][
                            "Decoder_LastBlock_CrossAttention"
                        ][j]
                    )
                )  # dim 0 of image_batch is now number of heads
                batch_plot_path = (
                    f"{tag}_Decoder_Final_Attention/{file.numpy().decode('utf-8')}"
                )
                self.add_image(
                    str(batch_plot_path), tf.expand_dims(tf.expand_dims(image, 0), -1)
                )

    def mel(self, mel, tag=""):
        img = tf.transpose(mel)
        figure = self._audio.display_mel(img, is_normal=True)
        buf = buffer_image(figure)
        img_tf = tf.image.decode_png(buf.getvalue(), channels=3)
        self.add_image(tag, tf.expand_dims(img_tf, 0))

    def image(self, image, with_bar=False, figsize=None, tag=""):
        buf = plot_image(image, with_bar=with_bar, figsize=figsize)
        image = tf.image.decode_png(buf.getvalue(), channels=4)
        image = tf.expand_dims(image, 0)
        self.add_image(tag=tag, image=image)

    def plot_1d(self, y, x=None, figsize=None, tag=""):
        buf = plot_1d(y, x=x, figsize=figsize)
        image = tf.image.decode_png(buf.getvalue(), channels=4)
        image = tf.expand_dims(image, 0)
        self.add_image(tag=tag, image=image)

    @control_frequency
    def loss(self, loss, losses = {}, tag="", **_):
        self.add_scalars(tag=f"{tag}/losses", dictionary=losses)
        self.add_scalar(tag=f"{tag}/loss", scalar_value=loss)

    @control_frequency
    def scalar(self, tag, scalar_value, **_):
        self.add_scalar(tag=tag, scalar_value=scalar_value)

    def audio(self, tag, mel, description=None):
        wav = tf.transpose(mel)
        wav = self._audio.reconstruct_waveform(wav)
        wav = tf.expand_dims(wav, 0)
        wav = tf.expand_dims(wav, -1)
        self.add_audio(
            tag, wav.numpy(), sr=self.config["sampling_rate"], description=description
        )
