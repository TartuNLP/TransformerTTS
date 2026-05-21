import logging
import tensorflow as tf

from transformer_tts.utils.argparser import tts_argparser
from transformer_tts.utils.training_config_manager import TrainingConfigManager
from transformer_tts.utils.scripts_utils import dynamic_memory_allocation


def main():
    parser = tts_argparser()
    args = parser.parse_args()

    tf.get_logger().propagate = False
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=args.log_level.upper(),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logger.setLevel(args.log_level.upper())

    for arg in vars(args):
        logger.info(f"{arg}: {getattr(args, arg)}")

    config = TrainingConfigManager(**vars(args))
    config.print_config()
    dynamic_memory_allocation(debug=args.debug)

    if config.mode == "train":
        from transformer_tts.workflows.train_tts import main as train_tts_main

        train_tts_main(args, config)
    elif config.mode == "predict":
        from transformer_tts.workflows.predict_tts import main as predict_main

        predict_main(args, config)
    elif config.mode == "save_model":
        from transformer_tts.workflows.checkpoints_to_weights import main as extract_weights_main

        extract_weights_main(args, config)
    else:
        raise ValueError(f"Unknown mode: {config.mode}")
