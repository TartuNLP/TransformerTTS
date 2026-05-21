import logging
from argparse import Namespace
from transformer_tts.utils.training_config_manager import TrainingConfigManager

logger = logging.getLogger(__name__)

def main(args: Namespace, config: TrainingConfigManager):
    model = config.load_checkpoint(
        checkpoint_path=args.checkpoint_path  # None defaults to latest
    )
    config.save_weights(model, target_dir=args.target_dir)

    logger.info("Done.")
