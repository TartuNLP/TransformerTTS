import logging
from pathlib import Path
from enum import Enum

from transformer_tts.utils.training_config_manager import TrainingConfigManager


logger = logging.getLogger(__name__)


class DataKind(str, Enum):
    TRAIN = "train_metadata_path"
    VALID = "valid_metadata_path"


class DataReader:
    def __init__(
        self,
        metadata_path: Path,
        multispeaker: None | str = None,
        n_languages: int = 1,
        column_sep="|",
    ):
        self.metadata_path = Path(metadata_path)
        self.multispeaker = multispeaker
        self.n_languages = n_languages
        self.column_sep = column_sep

        self.text_dict, self.filenames = self.read_metadata()

    def read_metadata(self):
        text_dict = {}
        with open(self.metadata_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                l_split = line.split(self.column_sep)
                filename, text = l_split[0], l_split[1]
                if filename.endswith(".wav"):
                    filename = filename[:-4]
                text = text.replace("\n", "")

                speaker = int(l_split[2]) if self.multispeaker is not None else 0
                language = int(l_split[3]) if self.n_languages > 1 else 0
                text_dict.update({filename: (text, speaker, language)})

        return text_dict, list(text_dict.keys())

    @classmethod
    def from_config(
        cls, config_manager: TrainingConfigManager, kind: DataKind
    ):
        metadata_path = getattr(config_manager, kind.value)
        return cls(
            metadata_path=metadata_path,
            multispeaker=config_manager.config["multispeaker"],
            n_languages=config_manager.config.get("n_languages", 1),
        )
