import logging
import tensorflow as tf

logger = logging.getLogger(__name__)


def dynamic_memory_allocation(debug=False):
    if debug:
        tf.debugging.disable_traceback_filtering()  # show full internal stack
        tf.config.run_functions_eagerly(True)  # debug-friendly (slow)
        tf.data.experimental.enable_debug_mode()  # TF 2.13+; makes dataset run eagerly-ish
    gpus = tf.config.experimental.list_physical_devices("GPU")
    if gpus:
        try:
            # Currently, memory growth needs to be the same across GPUs
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
            logical_gpus = tf.config.experimental.list_logical_devices("GPU")
            logger.info(f"{len(gpus)} Physical GPUs, {len(logical_gpus)} Logical GPUs")
        except Exception:
            logging.exception("Unknown error.")
