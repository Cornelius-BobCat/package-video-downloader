# youtube_downloader

VideoSoundAnalyzer is a Python package that allows you to download videos from YouTube, extract audio and frames from local videos, and analyze the intervals where there is sound in the extracted audio.

----> [Github](https://github.com/Cornelius-BobCat/package-video-downloader)

## Features

- Download videos from YouTube
- Extract audio from a video
- Extract frames from a video
- Analyze the intervals where there is sound in the extracted audio
- Save the sound intervals to a JSON file

## Installation

You can install VideoSoundAnalyzer from PyPI using `pip`:

## Usage

Here's an example of how to use the package:

```python
from youtube_downloader import VideoDownloader, AudioExtractor, SoundIntervalAnalyzer

# Download a video from YouTube
downloader = VideoDownloader(video_url, output_directory)
video_path = downloader.download_video()

# Extract frame of frame : select a intervals
frame_extractor = FrameExtractor(video_path, output_directory, quality, oneperframe )
frame_extractor.extract_frames()

# Extract audio from the downloaded video
if video_path:
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
