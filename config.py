""" All the configuration options for this program.

:param OUTPUT_DIR_NAME: A string, the name of the directory where the video and audio files are/will be stored (ENSURE THIS DIRECTORY ISN'T USED FOR ANYTHING ELSE.)
:param YT_URL: A string, the URL of the YouTube video to be downloaded and played.
:param YT_DOWNLOAD: A boolean, whether the video will be downloaded or not (if not, the video and audio files in OUTPUT_DIR will be used.)
:param OUTPUT_NAME_VIDEO: A string, the name of the video file downloaded and played (MUST CONTAIN .mp4 FILE EXTENSION.)
:param OUTPUT_NAME_AUDIO: A string, the name of the audio file downloaded and played (MUST CONTAIN .m4a FILE EXTENSION.)
:param SCALE: An int, the scale of the video in relation to a 144p video.
:param CHAR_SET: An int, the character set used when playing the video. These character sets can be found in the mp4totext.py file.
"""

"""CHANGE THESE"""
OUTPUT_DIR_NAME = "tmp"
YT_URL = "https://www.youtube.com/watch?v=FtutLA63Cp8"
YT_DOWNLOAD = True # Set to false if the video and audio have both already been downloaded
OUTPUT_NAME_VIDEO = "video.mp4" # MUST CONTAIN .mp4 FILE EXTENSION
OUTPUT_NAME_AUDIO = "audio.m4a" # MUST CONTAIN .m4a FILE EXTENSION
SCALE = 0.5 # Recommended set to 0.5
CHAR_SET = 4

"""IGNORE THIS"""
import os

if os.name == "nt": OUTPUT_DIR = f".\\{OUTPUT_DIR_NAME}\\" # Windows
else: OUTPUT_DIR = f"./{OUTPUT_DIR_NAME}/" # Unix

OUTPUT_VIDEO_DIR = OUTPUT_DIR + OUTPUT_NAME_VIDEO
OUTPUT_AUDIO_DIR = OUTPUT_DIR + OUTPUT_NAME_AUDIO

if not OUTPUT_NAME_VIDEO.endswith(".mp4"):
    raise ValueError("Output video file name must contain the \".mp4\" file extension...")
if not OUTPUT_NAME_AUDIO.endswith(".m4a"):
    raise ValueError("Output audio file name must contain the \".m4a\" file extension...")
if SCALE <= 0:
    raise ValueError("Scale must be a positive integer above 0...")
if CHAR_SET not in range(1, 6):
    raise ValueError("CHAR_SET must be between 1 and 5 (inclusive)")
