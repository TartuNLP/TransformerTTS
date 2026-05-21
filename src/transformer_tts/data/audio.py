import librosa
import numpy as np
import librosa.display
from matplotlib import pyplot as plt


class Audio:
    def __init__(
        self,
        sampling_rate: int,
        n_fft: int,
        hop_length: int,
        win_length: int,
        f_min: int,
        f_max: int,
        **_,
    ):
        self.sampling_rate = sampling_rate
        self.n_fft = n_fft
        self.hop_length = hop_length
        self.win_length = win_length
        self.f_min = f_min
        self.f_max = f_max

    def _denormalize(self, s):
        return np.exp(s)

    def reconstruct_waveform(self, mel, n_iter=32):
        """Uses Griffin-Lim phase reconstruction to convert from a normalized
        mel spectrogram back into a waveform."""
        amp_mel = self._denormalize(mel)
        s = librosa.feature.inverse.mel_to_stft(
            amp_mel,
            power=1,
            sr=self.sampling_rate,
            n_fft=self.n_fft,
            fmin=self.f_min,
            fmax=self.f_max,
        )
        wav = librosa.core.griffinlim(
            s, n_iter=n_iter, hop_length=self.hop_length, win_length=self.win_length
        )
        return wav

    def display_mel(self, mel, is_normal=True):
        if is_normal:
            mel = self._denormalize(mel)
        f, ax = plt.subplots(figsize=(10, 4))
        s_db = librosa.power_to_db(mel, ref=np.max)
        img = librosa.display.specshow(
            s_db,
            x_axis="time",
            y_axis="mel",
            sr=self.sampling_rate,
            fmin=self.f_min,
            fmax=self.f_max,
            ax=ax,
        )
        f.colorbar(img, ax=ax, format="%+2.0f dB")
        ax.set(title="Mel-Spectrogram")
        f.tight_layout()

        return f

    def save_wav(self, y, wav_path):
        import soundfile as sf

        sf.write(wav_path, data=y, samplerate=self.sampling_rate)

    @classmethod
    def from_config(cls, config: dict):
        return cls(**config)
