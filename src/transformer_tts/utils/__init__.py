from pathlib import Path
from .training_config_manager import TrainingConfigManager, ForwardTransformer

def load_weights(path: Path, check_version=True) -> ForwardTransformer:
    return TrainingConfigManager.load_weights(path, check_version=check_version)