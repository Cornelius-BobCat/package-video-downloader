from moviepy.editor import VideoFileClip
import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class AudioExtractor:
    """
    A class that extracts audio from a video file.

    Args:
        video_path (str): The path to the video file.
        output_path (str): The path to save the extracted audio file.

    Attributes:
        video_path (str): The path to the video file.
        output_path (str): The path to save the extracted audio file.
        logger (logging.Logger): The logger instance for logging messages.

    """

    def __init__(self, video_path, output_path):
        self.video_path = video_path
        self.output_path = output_path
        self.logger = logging.getLogger(__name__)

    def extract_audio(self):
        """
        Extracts the audio from the video file and saves it to the output path.

        Raises:
            Exception: If there is an error during the audio extraction.

        """
        try:
            clip = VideoFileClip(self.video_path)
            audio = clip.audio
            audio.write_audiofile(self.output_path)
            self.logger.info("Extract audio ok !")
        except Exception as e:
            self.logger.error(f"Error extract audio : {e}")
