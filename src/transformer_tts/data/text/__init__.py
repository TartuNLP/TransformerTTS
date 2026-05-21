from transformer_tts.data.text.tokenizer import Phonemizer, Tokenizer
import tensorflow as tf


class TextToTokens:
    def __init__(self, phonemizer: Phonemizer, tokenizer: Tokenizer):
        self.phonemizer = phonemizer
        self.tokenizer = tokenizer

    def __call__(
        self, input_text: str | list, speaker_id: int | list[int] = 0
    ) -> tf.Tensor:
        phons = self.phonemizer(input_text)
        tokens = self.tokenizer(phons, speaker_id)
        if isinstance(input_text, list):
            tokens = tf.keras.preprocessing.sequence.pad_sequences(
                tokens, padding="post", value=0
            )
        tokens = tf.cast(tokens, tf.int32)
        return tokens

    @classmethod
    def default(
        cls,
        alphabet: str,
        gst: bool = False,
        zfill: int = 0,
    ):
        phonemizer = Phonemizer(
            alphabet=alphabet,
        )
        tokenizer = Tokenizer(
            alphabet=alphabet,
            gst=gst,
            zfill=zfill,
        )
        return cls(phonemizer=phonemizer, tokenizer=tokenizer)
