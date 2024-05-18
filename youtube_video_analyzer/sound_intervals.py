import numpy as np
import logging
import librosa
import json

# Configurer le niveau de journalisation
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class SoundIntervalAnalyzer:
    """
    Class for analyzing sound intervals in an audio file.

    Args:
        audio_path (str): Path to the audio file.
        n_fft (int, optional): Number of FFT points. Defaults to 2048.
        hop_length (int, optional): Number of samples between successive frames. Defaults to 512.
        threshold_db (float, optional): Threshold in decibels below which a frame is considered silence. Defaults to -40.
        min_silence_duration (float, optional): Minimum duration of silence in seconds to be considered as an interval. Defaults to 0.2.
        output_json (str, optional): Path to the output JSON file to save the sound intervals. Defaults to "sound_intervals.json".

    Attributes:
        audio_path (str): Path to the audio file.
        n_fft (int): Number of FFT points.
        hop_length (int): Number of samples between successive frames.
        threshold_db (float): Threshold in decibels below which a frame is considered silence.
        min_silence_duration (float): Minimum duration of silence in seconds to be considered as an interval.
        output_json (str): Path to the output JSON file to save the sound intervals.
        logger (logging.Logger): Logger object for logging messages.

    Methods:
        create_sound_intervals_json: Analyzes the sound intervals in the audio file and saves them to a JSON file.
    """

    def __init__(
        self,
        audio_path,
        n_fft=2048,
        hop_length=512,
        threshold_db=-40,
        min_silence_duration=0.2,
        output_json="sound_intervals.json",
    ):
        self.audio_path = audio_path
        self.n_fft = n_fft
        self.hop_length = hop_length
        self.threshold_db = threshold_db
        self.min_silence_duration = min_silence_duration
        self.output_json = output_json
        self.logger = logging.getLogger(__name__)

    def create_sound_intervals_json(self):

        try:
            y, sr = librosa.load(self.audio_path)
            D = librosa.stft(y, n_fft=self.n_fft, hop_length=self.hop_length)
            D_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
            sound_intervals = []
            start_silence = None
            for t in range(D_db.shape[1]):
                if np.max(D_db[:, t]) > self.threshold_db:
                    if start_silence is None:
                        start_silence = librosa.frames_to_time(
                            t, sr=sr, hop_length=self.hop_length
                        )
                else:
                    if start_silence is not None:
                        end_silence = librosa.frames_to_time(
                            t, sr=sr, hop_length=self.hop_length
                        )
                        if end_silence - start_silence >= self.min_silence_duration:
                            sound_intervals.append((start_silence, end_silence))
                        start_silence = None
            if self.output_json:
                with open(self.output_json, "w") as json_file:
                    json.dump(sound_intervals, json_file, indent=2)
                self.logger.info(f"Intervals are save {self.output_json}.")
        except Exception as e:
            self.logger.error(f"Error when analysis : {e}")
