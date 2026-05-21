import logging
from pathlib import Path
from enum import Enum

import numpy as np
import ruamel.yaml

from transformer_tts.model.forward_model import ForwardTransformer
from transformer_tts.version import get_version

logger = logging.getLogger(__name__)

class TTSMode(str, Enum):
    TRAIN = "train"
    PREDICT = "predict"
    WEIGHTS = "save_model"


class TrainingConfigManager:
    def __init__(
        self,
        mode: TTSMode = TTSMode.PREDICT,
        config_path: str | None = None,
        seed: int | None = None,
        save_directory: str = "",
        mel_directory: str = "mels",
        duration_directory: str = "duration",
        character_pitch_directory: str = "char_pitch",
        check_version: bool = True,
        **_,
    ):
        self.mode = mode
        self.save_directory = Path(save_directory)
        self.log_dir = self.save_directory / "logs"
        self.weights_dir = self.save_directory / "weights"

        if config_path is None:
            config_path = str(self.weights_dir / "config.yaml")

        self.yaml = ruamel.yaml.YAML()
        self.config = self._load_config(config_path)
        if check_version:
            version = get_version()
            if self.config.get("version") != version:
                logger.warning(
                    f"Version mismatch. Current version: {version}. Version in config: {self.config['version']}"
                )

        self.data_dir = self.save_directory / "metadata"
        self.train_metadata_path = self.data_dir / "train_metadata.txt"
        self.valid_metadata_path = self.data_dir / "valid_metadata.txt"

        self.mel_dir = Path(mel_directory)
        self.duration_dir = Path(duration_directory)
        self.pitch_per_char = Path(character_pitch_directory)

        # training parameters
        self.learning_rate = np.array(self.config["learning_rate_schedule"])[
            0, 1
        ].astype(np.float32)

        self.seed = seed
        if seed is not None:
            np.random.seed(seed)
            import tensorflow as tf

            tf.random.set_seed(seed)

        if self.mode == TTSMode.TRAIN:
            self.save_directory.mkdir(exist_ok=True, parents=True)
            self.log_dir.mkdir(exist_ok=True)
            self.weights_dir.mkdir(exist_ok=True)
            self.dump_config()

    def _load_config(self, config_path):
        config_path = Path(config_path)
        with open(str(config_path), "rb") as session_yaml:
            session_config = self.yaml.load(session_yaml)

        if session_config.get("automatic", False):
            session_config = {k.lower(): v for k, v in session_config.items()}
            session_config["version"] = session_config.get("version", None)
            return session_config
        else:
            all_config = {}
            for key in [
                "dataset",
                "audio_settings",
                "model_settings",
            ]:
                subconfig = {k.lower(): v for k, v in session_config[key].items()}
                all_config.update(subconfig)
            all_config["version"] = get_version()
            return all_config

    @staticmethod
    def _print_dict_values(values, key_name, level=0, tab_size=2):
        tab = level * tab_size * " "
        logger.info(f"{tab}- {key_name}: {values}")

    def _print_dictionary(self, dictionary, recursion_level=0):
        for key in dictionary.keys():
            if isinstance(key, dict):
                recursion_level += 1
                self._print_dictionary(dictionary[key], recursion_level)
            else:
                self._print_dict_values(
                    dictionary[key], key_name=key, level=recursion_level
                )

    def print_config(self):
        config_text = "\n\t".join(["CONFIGURATION:"] + [f"{k}: {v}" for k, v in self.config.items()])
        logger.info(config_text)

    def update_config(self):
        self.config["version"] = get_version()
        self.config["automatic"] = True

    def get_model(self) -> ForwardTransformer:
        """
        Get the model instance based on the configuration.
        The model is compiled with the appropriate optimizer and learning rate schedule.
        """
        model = ForwardTransformer.from_config(self.config)
        self.compile_model(model)
        return model

    def compile_model(self, model, beta_1=0.9, beta_2=0.98):
        import tensorflow as tf

        gradient_accumulation_steps = self.config.get("gradient_accumulation_steps")
        if gradient_accumulation_steps == 1:
            gradient_accumulation_steps = None
        optimizer = tf.keras.optimizers.Adam(
            float(self.learning_rate),
            beta_1=beta_1,
            beta_2=beta_2,
            epsilon=1e-9,
            gradient_accumulation_steps=gradient_accumulation_steps,
        )
        model.compile_model(optimizer=optimizer)

    def dump_config(self):
        self.update_config()
        with open(self.weights_dir / "config.yaml", "w") as model_yaml:
            self.yaml.dump(self.config, model_yaml)

    def load_checkpoint(self, checkpoint_path: str | None = None, verbose=True):
        import tensorflow as tf

        model = self.get_model()
        ckpt = tf.train.Checkpoint(
            net=model, optimizer=model.optimizer, step=tf.Variable(1)
        )

        if checkpoint_path is not None:
            ckpt.restore(checkpoint_path)
            logger.info(f"restored weights from {checkpoint_path} at step {model.step}")
        else:
            manager = tf.train.CheckpointManager(
                ckpt, self.weights_dir, max_to_keep=None
            )
            if manager.latest_checkpoint is None:
                raise FileNotFoundError(f"No checkpoints found in {manager.directory}.")
            ckpt.restore(manager.latest_checkpoint)
            logger.info(
                f"restored weights from {manager.latest_checkpoint} at step {model.step}"
            )

        return model

    def save_weights(self, model, target_dir: Path | None = None):
        if target_dir is None:
            target_dir = self.save_directory
        model.build((None, None))
        model.save(target_dir / "mdl.keras")
        logger.info(f"Model weights saved under {target_dir / 'mdl.keras'}")

    @classmethod
    def load_weights(cls, path: Path, check_version=True):
        weights_path = path / "mdl.keras"
        
        import tensorflow as tf
        model = tf.keras.models.load_model(weights_path)

        return model
