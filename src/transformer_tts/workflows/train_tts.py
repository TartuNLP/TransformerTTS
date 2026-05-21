import logging
from argparse import Namespace

import tensorflow as tf
from tqdm import trange

from transformer_tts.data.metadata_readers import DataKind
from transformer_tts.data.datasets import Dataset as TTSDataset
from transformer_tts.model import ForwardTransformer
from transformer_tts.model.scheduling import piecewise_linear_schedule
from transformer_tts.utils.training_config_manager import TrainingConfigManager
from transformer_tts.utils.logging_utils import SummaryManager

logger = logging.getLogger(__name__)


def validate(model: ForwardTransformer, dataset: TTSDataset, tb: SummaryManager):
    val_loss = 0.0
    val_losses = {"mel": 0.0, "duration": 0.0, "pitch": 0.0}
    norm = 0

    for i, data in enumerate(dataset.all_batches()):
        mel, phonemes, durations, pitch, speaker_id, language_id = data
        output = model.val_step(
            input_sequence=phonemes,
            target_sequence=mel,
            target_durations=durations,
            target_pitch=pitch,
            speaker_id=speaker_id,
            language_id=language_id,
        )

        norm += 1
        val_loss += float(output["loss"])
        for loss in output["losses"].keys():
            val_losses[loss] += float(output["losses"][loss])

        try:
            i_len = tf.math.reduce_sum(tf.cast(phonemes != 0, dtype=tf.int32), axis=1)[0]
        except Exception as e:
            logger.error(f"Error calculating input length for validation sample {i}: {e}")
            print(f"phonemes: {phonemes}")
            print(f"durations: {durations}")
            print(f"pitch: {pitch}")
            print(f"speaker_id: {speaker_id}")
            print(f"language_id: {language_id}")
            continue
        o_len = tf.math.reduce_sum(durations, axis=1)[0]
        tb.plot_1d(
            tag=f"Validation/{i} predicted pitch",
            y=output["pitch"][0][:i_len],
        )
        tb.plot_1d(tag=f"Validation/{i} target pitch", y=pitch[0][:i_len])
        tb.plot_1d(
            tag=f"Validation/{i} predicted dur",
            y=output["duration"][0][:i_len],
        )
        tb.plot_1d(tag=f"Validation/{i} target dur", y=durations[0][:i_len])
        tb.mel(
            tag=f"Validation/{i} predicted_mel_forced",
            mel=output["mel"][0][:o_len],
        )
        tb.mel(tag=f"Validation/{i} target_mel", mel=mel[0][:o_len])
        tb.audio(tag=f"Validation/{i} prediction_forced", mel=output["mel"][0][:o_len])
        tb.audio(tag=f"Validation/{i} target", mel=mel[0][:o_len])

        # predict without enforcing durations and pitch
        output = model.predict(
            phonemes[:1][:i_len],
            encode=False,
            speaker_id=speaker_id[:1],
            language_id=language_id[:1],
        )
        tb.mel(tag=f"Validation/{i} predicted_mel", mel=output["mel"][0])
        tb.audio(tag=f"Validation/{i} prediction", mel=output["mel"][0])

    val_loss = val_loss / norm
    val_losses = {k: v / norm for k, v in val_losses.items()}

    tb.loss(loss=val_loss, losses=val_losses, tag="Validation", plot_all=True)
    return val_loss


def test(model: ForwardTransformer, test_snts: list, tb: SummaryManager):
    texts = [line[0] for line in test_snts]
    speaker_ids = [int(line[1]) for line in test_snts]
    language_ids = [int(line[2]) for line in test_snts]

    out = model.predict(
        texts, encode=True, speaker_id=speaker_ids, language_id=language_ids
    )
    o_lens = tf.squeeze(tf.cast(tf.math.reduce_sum(out["duration"], axis=1), tf.int32))
    for i, line in enumerate(texts):
        mel = out["mel"][i][: o_lens[i]]
        tb.mel(tag=f"Test/{i} predicted_mel", mel=mel)
        tb.audio(tag=f"Test/{i} predicted_audio", mel=mel, description=line)


def main(args: Namespace, config: TrainingConfigManager):
    model: ForwardTransformer = config.get_model() # type: ignore

    tensorboard = SummaryManager(
        model=model, log_dir=config.log_dir, config=config.config
    )

    train_dataset = TTSDataset.from_config(
        config=config,
        tokenizer=model.text_pipeline.tokenizer,
        kind=DataKind.TRAIN,
        bucket_batch_sizes=config.config["bucket_batch_sizes"],
        bucket_boundaries=config.config["bucket_boundaries"],
        shuffle=True,
    )
    valid_dataset = TTSDataset.from_config(
        config=config,
        tokenizer=model.text_pipeline.tokenizer,
        kind=DataKind.VALID,
        bucket_batch_sizes=config.config["val_bucket_batch_size"],
        bucket_boundaries=config.config["bucket_boundaries"],
        shuffle=False,
    )

    checkpoint = tf.train.Checkpoint(
        step=tf.Variable(1), optimizer=model.optimizer, net=model
    )

    checkpoint_manager = tf.train.CheckpointManager(
        checkpoint=checkpoint,
        directory=str(config.weights_dir),
        max_to_keep=config.config["keep_n_weights"],
    )

    logger.info(f"Last checkpoint: {checkpoint_manager.latest_checkpoint}")
    checkpoint.restore(checkpoint_manager.latest_checkpoint)
    logger.info(f"Training from step {model.step}")

    test_snts = []
    for test_file in args.test_files:
        with open(test_file, "r") as f:
            for test_line in f.readlines():
                parts = test_line.strip().split("|")
                text = parts[0]
                speaker_id = int(parts[1]) if len(parts) > 1 else 0
                language_id = int(parts[2]) if len(parts) > 2 else 0
                test_snts.append((text, speaker_id, language_id))

    losses = []
    loss_stats = {}
    gradient_acc_steps = config.config.get("gradient_accumulation_steps")
    gradient_acc_steps = 1 if gradient_acc_steps is None else gradient_acc_steps

    t = trange(
        0,
        config.config["max_steps"],
        initial=model.step,
        leave=True,
        dynamic_ncols=True,
    )

    try:
        for _ in t:
            _loss = 0.0
            _losses = {"mel": 0.0, "duration": 0.0, "pitch": 0.0}
            batch_size = 0
            for j in range(gradient_acc_steps):
                t.set_description(f"step {model.step} ({j + 1}/{gradient_acc_steps})")
                mel, phonemes, durations, pitch, speaker_id, language_id = (
                    train_dataset.next_batch()
                )
                learning_rate = piecewise_linear_schedule(
                    model.step, config.config["learning_rate_schedule"]
                )
                model.set_constants(learning_rate=learning_rate)
                output = model.train_step(
                    input_sequence=phonemes,
                    speaker_id=speaker_id,
                    language_id=language_id,
                    target_sequence=mel,
                    target_durations=durations,
                    target_pitch=pitch,
                )

                batch_size += output["mel"].shape[0]

                _loss += float(output["loss"])
                for k, v in output["losses"].items():
                    _losses[k] += v

            tensorboard.scalar(scalar_value=batch_size, tag="Meta/batch_size")
            tensorboard.scalar(
                tag="Meta/learning_rate", scalar_value=model.optimizer.learning_rate
            )

            losses.append(_loss)
            tensorboard.loss(loss=_loss, losses=_losses, tag="Train")
            loss_stats["step_loss"] = losses[-1]
            
            for n_steps in config.config["n_steps_avg_losses"]:
                if len(losses) > n_steps:
                    loss_stats[f"{n_steps}_step_loss"] = (
                        sum(losses[-n_steps:]) / n_steps
                    )
                else:
                    loss_stats[f"{n_steps}_step_loss"] = "-"

            if model.step % config.config["train_images_plotting_frequency"] == 0:
                tensorboard.mel(mel=output["mel"][0], tag="Train/predicted_mel")
                tensorboard.mel(mel=mel[0], tag="Train/target_mel")
                tensorboard.plot_1d(tag="Train/Predicted pitch", y=output["pitch"][0])
                tensorboard.plot_1d(tag="Train/Target pitch", y=pitch[0])

            if model.step % config.config["weights_save_frequency"] == 0:
                checkpoint_manager.save(checkpoint_number=model.step)

            if model.step % config.config["validation_frequency"] == 0:
                val_loss = validate(model=model, dataset=valid_dataset, tb=tensorboard)
                loss_stats["val_loss"] = val_loss

            t.set_postfix(loss_stats)

            if model.step % config.config["prediction_frequency"] == 0:
                if model.step >= config.config["prediction_start_step"]:
                    test(model, test_snts, tensorboard)

        logger.info("Done.")
    except KeyboardInterrupt:
        logger.info("Training interrupted. Saving checkpoint.")
    finally:
        checkpoint_manager.save(checkpoint_number=model.step)
        logger.info(f"Checkpoint saved at step {model.step}.")
