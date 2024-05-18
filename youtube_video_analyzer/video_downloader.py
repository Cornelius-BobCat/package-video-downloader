from pytube import YouTube
import os
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class VideoDownloader:
    """
    A class that represents a video downloader.

    Attributes:
        url (str): The URL of the video to be downloaded.
        output_path (str): The path where the downloaded video will be saved.
        name (str): The name of the downloaded video file (default is "video.mp4").
        logger (logging.Logger): The logger object for logging messages.

    Methods:
        download_video: Downloads the video from the specified URL and saves it to the output path.
    """

    def __init__(self, url, output_path, name="video.mp4"):
        """
        Initializes a new instance of the VideoDownloader class.

        Args:
            url (str): The URL of the video to be downloaded.
            output_path (str): The path where the downloaded video will be saved.
            name (str, optional): The name of the downloaded video file (default is "video.mp4").
        """
        self.url = url
        self.output_path = output_path
        self.name = name
        self.logger = logging.getLogger(__name__)

    def download_video(self):
        """
        Downloads the video from the specified URL and saves it to the output path.

        Returns:
            str: The path of the downloaded video file if successful, None otherwise.
        """
        try:
            yt = YouTube(self.url)
            name = self.name

            video = yt.streams.filter(progressive=True, file_extension="mp4").first()
            if video:
                video.download(self.output_path, name)
                self.logger.info("Download ok!")
                self.logger.debug(f"Nom du fichier : {video.default_filename}")
                return os.path.join(self.output_path, name)
            else:
                self.logger.warning("That video is not available in mp4 format.")
                return None
        except Exception as e:
            self.logger.error(f"Error downloader: {str(e)}")
            return None
