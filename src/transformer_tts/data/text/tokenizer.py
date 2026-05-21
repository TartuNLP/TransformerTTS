from transformer_tts.data.text.symbols import gst_tokens


class Tokenizer:
    def __init__(self, alphabet: str, pad_token="/", gst=False, zfill=0):
        self.alphabet = alphabet

        self.gst = gst
        self.zfill = 0
        if self.gst:
            self.alphabet += gst_tokens
            self.zfill = zfill

        self.alphabet = sorted(list(set(self.alphabet)))

        self.idx_to_token = {i: s for i, s in enumerate(self.alphabet, start=1)}
        self.idx_to_token[0] = pad_token
        self.token_to_idx = {s: [i] for i, s in self.idx_to_token.items()}
        self.vocab_size = len(self.alphabet) + 1

    def __call__(
        self, sentence: str | list[str], speaker_id: int | list[int] = 0
    ) -> list:
        if isinstance(sentence, list):
            if isinstance(speaker_id, list):
                return [self.encode(s, sid) for s, sid in zip(sentence, speaker_id)]
            else:
                return [self.encode(s, speaker_id) for s in sentence]
        elif isinstance(speaker_id, int):
            return self.encode(sentence, speaker_id)
        else:
            raise ValueError("speaker_id should be either int or list of int")

    def encode(self, snt: str, speaker_id: int) -> list:
        sentence = str(speaker_id).zfill(self.zfill) + snt if self.gst else snt
        try:
            sequence = [
                self.token_to_idx[c] for c in sentence
            ]  # No filtering: text should only contain known chars.
        except KeyError as e:
            raise ValueError(
                f"Character {e.args[0]} is not in the vocabulary, sentence: {sentence}, speaker_id: {speaker_id}"
            )
        sequence = [item for items in sequence for item in items]
        return sequence

    def decode(self, sequence: list) -> str:
        return "".join([self.idx_to_token[int(t)] for t in sequence])


class Phonemizer:
    def __init__(self, alphabet: str):
        self.alphabet = sorted(list(set(alphabet)))

    def __call__(self, text: str | list[str]) -> str | list[str]:
        if isinstance(text, list):
            return [self._process_string(t) for t in text]
        else:
            return self._process_string(text)

    def _process_string(self, text: str) -> str:
        text = "".join([c for c in text if c in self.alphabet])
        text = text.strip()
        return text
