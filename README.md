# Transformer-based Text-to-Speech in TensorFlow 2

Implementation of a non-autoregressive Transformer-based neural network for Text-to-Speech (TTS).

This is repository is managed by [TartuNLP](https://tartunlp.ai), and it is a fork of the implementation
by [Axel Springer](https://github.com/as-ideas/TransformerTTS). Our contributions compared to the original repository
are:

- Support for grapheme-based synthesis
- Multi-speaker synthesis
- [Pretrained models](https://github.com/TartuNLP/TransformerTTS/releases) for Estonian
- Open source TTS applications:
  - [API](https://github.com/TartuNLP/text-to-speech-api)
      \+ [worker](https://github.com/TartuNLP/text-to-speech-worker) combo.
- Numerous minor changes to streamline training and make the repository easier to use with new datasets.

When using this repository or models for research, please cite the following paper:

```bibtex
@article{R2tsep_2022,
  title = {Estonian Text-to-Speech Synthesis with Non-autoregressive Transformers},
  author = {Liisa R\"{a}tsep and Rasmus Lellep and Mark Fishel},
  journal = {Baltic Journal of Modern Computing}
  volume = {10},
  number = {3},
  year = 2022 
}
```

The original code is based, among others, on the following papers:

- [Neural Speech Synthesis with Transformer Network](https://arxiv.org/abs/1809.08895)
- [FastSpeech: Fast, Robust and Controllable Text to Speech](https://arxiv.org/abs/1905.09263)
- [FastSpeech 2: Fast and High-Quality End-to-End Text to Speech](https://arxiv.org/abs/2006.04558)
- [FastPitch: Parallel Text-to-speech with Pitch Prediction](https://fastpitch.github.io/)

The models are compatible with the pre-trained vocoders:

- [MelGAN](https://github.com/seungwonpark/melgan)
- [HiFiGAN](https://github.com/jik876/hifi-gan)
- [Speechbrain HiFiGAN](https://huggingface.co/speechbrain/tts-hifigan-libritts-22050Hz)

Being non-autoregressive, this Transformer model is:

- Robust: No repeats and failed attention modes for challenging sentences.
- Fast: With no autoregression, predictions take a fraction of the time.
- Controllable: It is possible to control the speed and pitch of the generated utterance.

## 🔈 Samples

Estonian and multispeaker samples can be found [on the samples page](https://tartunlp.github.io/TransformerTTS/).

Samples from the original implementation can be found [on the original samples page](https://tartunlp.github.io/TransformerTTS/original).

## Updates

- 05/26: Made into installable library and added a CLI (TartuNLP)
- 06/22: Multi-speaker synthesis (TartuNLP)
- 05/22: Merged updates from the original repository (TartuNLP)
- 06/21: Grapheme-based synthesis and Estonian models (TartuNLP)
- 06/20: Added normalisation and pre-trained models compatible with the
  faster [MelGAN](https://github.com/seungwonpark/melgan) vocoder.
- 11/20: Added pitch prediction. Autoregressive model is now specialized as an Aligner and Forward is now the only TTS
  model. Changed models architectures. Discontinued WaveRNN support. Improved duration extraction with Dijkstra
  algorithm.
- 03/20: Vocoding branch.

## 📖 Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Training](#training)
  - [Aligner](#train-aligner-model)
  - [TTS](#train-tts-model)
- [Prediction](#prediction)
- [Model Weights](#model-weights)

## Installation

The repository can be installed with pip:

```bash
pip install git+https://github.com/TartuNLP/TransformerTTS.git
```

For a specific version, the tag name:

```bash
pip install git+https://github.com/TartuNLP/TransformerTTS.git@v2.0.0
```

or locally from the source code:

```bash
git clone https://github.com/TartuNLP/TransformerTTS.git
cd TransformerTTS
pip install -e .
```

## Dataset

You can directly use [LJSpeech](https://keithito.com/LJ-Speech-Dataset/) to create the training dataset.

### Configuration

- If training on LJSpeech, or if unsure, simply use `config/training_config.yaml` to
  create [MelGAN](https://github.com/seungwonpark/melgan) or [HiFiGAN](https://github.com/jik876/hifi-gan) compatible
  models
- Use the command line flags to specify dataset location and where preprocessed data, logs and model files should be
  saved. Information about configuration flags can be seen with the `-h` flag of each script.

### Custom dataset

Prepare a folder containing your metadata and wav files, for instance

```text
dataset_folder/
├── metadata.csv
└── wavs/
    ├── file_1.wav
    ├── ...
    └── file_n.wav
```

if `metadata.csv` has the following format
`wav_file_name|transcription` or `wav_file_name|transcription|speaker_id`
you can use the ljspeech preprocessor in `data/metadata_readers.py`, otherwise add your own under the same file.

Make sure that:

- the metadata reader function name is the same as `metadata_reader` field in `training_config.yaml`.
- the metadata file (can be anything) is specified under `metadata_path` in `training_config.yaml`
- for multispeaker training, review the `multispeaker` and `n_speakers` values.
- to disable phonemization, edit the `text_settings` section of the configuration file.

## Training

Change the `--config` argument based on the configuration of your choice.

### Model training

```bash
transformer-tts train \
    --config $CONFIG_FILE_PATH \
    --save-directory $MODEL_PATH \
    --mel-directory $DATA_PATH/mels \
    --pitch-directory $DATA_PATH/pitch \
    --duration-directory $DATA_PATH/durations \
    --character-pitch-directory $DATA_PATH/char-pitch \
    --test-files $TEST_FILES
```

To resume training, simply use the same command with the same configuration and model path.
Training and model settings can be configured in `training_config.yaml`

#### Monitor training

```bash
tensorboard --logdir $MODEL_PATH/logs
```

### Extract model weights

```bash
transformer-tts save_model \
    --config $CONFIG_FILE_PATH \
    --save-directory $MODEL_PATH \
    --checkpoint-path $CHECKPOINT_PATH \
    --target-dir $WEIGHTS_PATH
```

The model will be saved as a `mdl.keras` file in the specified target directory. If no target directory is specified, the weights will be saved in the model root directory. If no checkpoint path is specified, the latest checkpoint will be used.

## Prediction

Prediction can be done using the `transformer-tts predict`, for the full specification, check the help flag of the command.

```bash
transformer-tts predict -h
```

Alternatively, to use the model in your own code, you can load the model directly in your code:

```python
import tensorflow as tf
from transformer_tts.model import ForwardTransformer
model = tf.keras.models.load_model(
    "mdl.keras",
    custom_objects={"ForwardTransformer": ForwardTransformer})

tts_out = model.predict(sentence, speed_regulator=speed, speaker_id=speaker_id)
mel_spec = tts_out["mel"].numpy().T
```

## Model Weights

Newer models are added to the [Releases](https://github.com/TartuNLP/TransformerTTS/releases) of this repository.

## Maintainers

[TartuNLP](https://tartunlp.ai) - the NLP research group at the University of Tartu.

## Special thanks

[Francesco Cardinale](https://github.com/cfrancesco) from Axel Springer for the original implementation.

[MelGAN](https://github.com/seungwonpark/melgan) and [WaveRNN](https://github.com/fatchord/WaveRNN): data normalization
and samples' vocoders are from these repos.

[Erogol](https://github.com/erogol) and the Mozilla TTS team for the lively exchange on the topic.

## Copyright

See [LICENSE](LICENSE) for details.
