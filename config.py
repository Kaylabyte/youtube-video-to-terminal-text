""" All the configuration options for this program.

:param OUTPUT_DIR: A string, the directory where the video and audio files are/will be stored.
:param YT_URL: A string, the URL of the YouTube video to be downloaded and played.
:param YT_DOWNLOAD: A boolean, whether the video will be downloaded or not (if not, the video and audio files in OUTPUT_DIR will be used.)
:param OUTPUT_VIDEO_NAME: A string, the name of the video file downloaded and played (MUST CONTAIN .mp4 FILE EXTENSION.)
:param OUTPUT_AUDIO_NAME: A string, the name of the audio file downloaded and played (MUST CONTAIN .m4a FILE EXTENSION.)
:param SCALE: An int, the scale of the video in relation to a 144p video.
:param CHAR_SET: An int, the character set used when playing the video. These character sets can be found in the mp4totext.py file.
"""

# CHANGE THESE
OUTPUT_DIR = "./tmp/" # Uncomment line on Unix/Linux, comment line out on Windows
# OUTPUT_DIR = ".\\tmp\\" # Uncomment line on Windows, comment line out on Unix/Linux
YT_URL = "https://www.youtube.com/watch?v=FtutLA63Cp8"
YT_DOWNLOAD = True
OUTPUT_VIDEO_NAME = "video.mp4" # MUST CONTAIN .mp4 FILE EXTENSION
OUTPUT_AUDIO_NAME = "audio.m4a" # MUST CONTAIN .m4a FILE EXTENSION
SCALE = 0.5 # Recommended set to 0.5
CHAR_SET = 4

# IGNORE THESE
OUTPUT_VIDEO_DIR = OUTPUT_DIR + OUTPUT_VIDEO_NAME
OUTPUT_AUDIO_DIR = OUTPUT_DIR + OUTPUT_AUDIO_NAME

