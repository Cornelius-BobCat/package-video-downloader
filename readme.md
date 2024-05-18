# youtube-video-analyzer

youtube-video-analyzer is a Python package that allows you to download videos from YouTube, extract audio and frames from local videos, and analyze the intervals where there is sound in the extracted audio.

----> [Github](https://github.com/Cornelius-BobCat/package-video-downloader)

## Features

- Download videos from YouTube
- Extract audio from a video
- Extract frames from a video
- Analyze the intervals where there is sound in the extracted audio
- Save the sound intervals to a JSON file

## Installation

You can install youtube-video-analyzer from PyPI using `pip install youtube-video-analyzer`:

## Usage

Here's an example of how to use the package:

```python
from youtube_video_analyzer import VideoDownloader, AudioExtractor, SoundIntervalAnalyzer, FrameExtractor

# Download a video from YouTube
downloader = VideoDownloader(video_url, output_directory)
video_path = downloader.download_video()

# Extract frame of frame : select a intervals
frame_extractor = FrameExtractor(video_path, output_directory, quality, oneperframe )
frame_extractor.extract_frames()

# Extract audio from the downloaded video
output_audio_path = "audio/source.mp3"
extractor = AudioExtractor(video_path, output_audio_path)
extractor.extract_audio()

# Analyze the sound intervals
analyzer = SoundIntervalAnalyzer(output_audio_path)
analyzer.create_sound_intervals_json()
```

## output json file extractor sound

```json
[
  [1.0448979591836736, 2.2058956916099772],
  [2.4380952380952383, 3.250793650793651],
  [4.1099319727891155, 4.620770975056689],
  [4.690430839002268, 5.5495691609977325],
  [5.7817687074829935, 6.339047619047619]
]
```

## arguments functions

```
VideoDownloader:
    -url (str): The URL of the video to be downloaded.
    -output_path (str): The path where the downloaded video will be saved.
    -name (str, optional): The name of the downloaded video file (default is "video.mp4").

FrameExtractor:
    -video_path (str): The path to the video file.
    -output_directory (str): The directory where the extracted frames will be saved.
    -quality (int, optional): The quality of the saved frames (default is 50).
    -oneperframe (int, optional): The number of frames to skip between extractions (default is 25).

AudioExtractor:
    -video_path (str): The path to the video file.
    -output_path (str): The path to save the extracted audio file.

AudioExtractor:
    -audio_path (str): Path to the audio file.
    -n_fft (int, optional): Number of FFT points. Defaults to 2048.
    -hop_length (int, optional): Number of samples between successive frames. Defaults to 512.
    -threshold_db (float, optional): Threshold in decibels below which a frame is considered silence. Defaults to -40.
    -min_silence_duration (float, optional): Minimum duration of silence in seconds to be considered as an interval. Defaults to 0.2.
    -output_json (str, optional): Path to the output JSON file to save the sound intervals. Defaults to "sound_intervals.json".
```

# License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Contributors

Cornélius vincent [linkedin](www.linkedin.com/in/corneliusvincent)

# Acknowledgments

This package utilizes the following libraries:

- pytube
- MoviePy
- librosa
- imageio
- NumPy
- json
- os
