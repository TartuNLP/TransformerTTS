from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from transformer_tts.utils.training_config_manager import TTSMode


def tts_argparser():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    
    subparsers = parser.add_subparsers(dest="mode", required=True, help="Mode of operation")
    training_parser = subparsers.add_parser(TTSMode.TRAIN.value, help="Train the TTS model.")
    predict_parser = subparsers.add_parser(TTSMode.PREDICT.value, help="Run inference with a trained model.")
    weights_parser = subparsers.add_parser(TTSMode.WEIGHTS.value, help="Extract and save weights from a checkpoint.")

    for subparser in [training_parser, predict_parser, weights_parser]:
        # General arguments for all modes
        subparser.add_argument('--config', dest='config_path', type=str, default=None, help="Path to the configuration file, defaults to the automatically saved config file in the model's directory.")
        subparser.add_argument('--seed', type=int, help="The seed value for model initialization and data shuffling.")
        subparser.add_argument('--log-level', type=str, help="Script logger level", default="INFO")
        subparser.add_argument('--save-directory', type=str, default="", help="Directory for training metadata, models and logs. Will be created if it doesn't exist.")
        subparser.add_argument('--debug', action='store_true', help="Debug mode, turns on tf eager debugging")

    # Subparser for TTS training
    training_parser.add_argument('--mel-directory', type=str, default="mels")
    training_parser.add_argument('--pitch-directory', type=str, default="pitch")
    training_parser.add_argument('--duration-directory', type=str, default="duration")
    training_parser.add_argument('--character-pitch-directory', type=str, default="char_pitch")
    training_parser.add_argument('--test-files', nargs='+', default=["test_files/test_sentences.txt"], help="A list of text files with one sentence per line to generate test samples. Predictions are stored in tensorboard logs.")

    # Subparser for prediction
    predict_parser.add_argument('--path', type=str, help="Optional path to a model, latest checkpoint will be loaded if not specified.")
    predict_parser.add_argument('--file', type=str, help="Text input file to be synthesized.")
    predict_parser.add_argument('--text', type=str, help="Text to be synthesized if an input file is not specified.")
    predict_parser.add_argument('--outdir', type=str, help="Directory for the output file.")
    predict_parser.add_argument('--store-mel', action='store_true', help="Also saves a Numpy array of the mel-spectrogram.")
    predict_parser.add_argument('--verbose', action='store_true', help="Verbose mode.")
    predict_parser.add_argument('--single', action='store_true', help="Saves each line of text in a separate file.")
    predict_parser.add_argument('--speaker-id', default=0, type=int, help="Speaker ID for multispeaker models.")

    # Subparser for weights extraction
    weights_parser.add_argument('--checkpoint-path', type=str, default=None, help="Checkpoint path, defaults to latest in the save directory.")
    weights_parser.add_argument('--target-dir', type=str, help="Directory to save the extracted weights.")

    return parser
