from moviepy.editor import VideoFileClip
import os
import imageio
import numpy as np
import logging


class FrameExtractor:
    """
    A class used to extract frames from a video file.

    Attributes:
        video_path (str): The path to the video file.
        output_directory (str): The directory where the extracted frames will be saved.
        quality (int): The quality of the saved frames (default is 50).
        oneperframe (int): The number of frames to skip between extractions (default is 25).
        logger (logging.Logger): The logger object for logging messages.

    Methods:
        extract_frames(): Extracts frames from the video file and saves them to the output directory.
    """

    def __init__(self, video_path, output_directory, quality=50, oneperframe=25):
        """
        Initializes a FrameExtractor object.

        Args:
            video_path (str): The path to the video file.
            output_directory (str): The directory where the extracted frames will be saved.
            quality (int, optional): The quality of the saved frames (default is 50).
            oneperframe (int, optional): The number of frames to skip between extractions (default is 25).
        """
        self.video_path = video_path
        self.output_directory = output_directory
        self.quality = quality
        self.oneperframe = oneperframe
        self.logger = logging.getLogger(__name__)

    def extract_frames(self):
        """
        Extracts frames from the video file and saves them to the output directory.
        """
        try:
            clip = VideoFileClip(self.video_path)
            fps = clip.fps
            duration = clip.duration
            frame_count = int(duration * fps)
            oneperframe = self.oneperframe

            for i in range(0, frame_count, oneperframe):
                frame_time = i / fps
                frame = clip.get_frame(frame_time)
                frame_name = f"frame_{i:04d}.jpg"
                frame_path = os.path.join(self.output_directory, frame_name)
                imageio.imwrite(frame_path, np.array(frame), quality=self.quality)
            self.logger.debug(f"Image {frame_name} save.")

        except Exception as e:
            self.logger.error(f"Error extract images : {e}")
