import os

try: # dependency check
    import pytubefix
    import cv2
    import pydub
except ImportError as error:
    raise ImportError(
        f"Missing dependency: {error.name}\nPlease refer to \"requirements.txt\" for the full list of "
        "required dependencies..."
    ) from error

import config
import videodownload
import mp4totext
import playtextvideo

def delete_output(output_dir):
    """Delete everything in the output folder."""
    try:
        output_dir_size = len(os.listdir(output_dir))
        output_dir_write_perms = os.access(output_dir, os.W_OK)

        if output_dir_size > 2: # safety checks, avoids accidentally deleting the wrong folder
            raise ValueError(
                f"This program has detected more files than expected ({output_dir_size}) in the output "
                "directory and has terminated itself for your safety.\nPlease ensure the output "
                "directory is correct, then try again..."
            )
        if not output_dir_write_perms:
            raise PermissionError(
                "No write permissions were found.\nPlease ensure you have write permissions for the "
                "output directory, then try again..."
            )
        for file_name in os.listdir(output_dir):
            if os.path.isdir(file_name):
                raise IsADirectoryError(
                    "Output directory contains a subfolder.\nPlease ensure the output directory is "
                    "correct and has no additional folders in it, then try again..."
                )

        for file_name in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, file_name))

    except NotADirectoryError as error:
        raise NotADirectoryError(
            f"\"{output_dir}\" is not a folder.\nPlease provide a valid folder name to OUTPUT_DIR "
            "(in the \"config.py\" file), then try again..."
        ) from error
    except FileNotFoundError:
        pass # no harm is done if there's nothing to delete to begin with :D

if __name__ == "__main__":
    if config.YT_DOWNLOAD:
        delete_output(config.OUTPUT_DIR) # ensures no additional files will affect anything
        videodownload.video_download(config.YT_URL, config.OUTPUT_DIR, config.OUTPUT_NAME_VIDEO,
            config.OUTPUT_NAME_AUDIO)

    video_terminal, fps = mp4totext.video_convert(config.OUTPUT_VIDEO_DIR, config.SCALE, config.CHAR_SET)
    playtextvideo.play_video(config.OUTPUT_AUDIO_DIR, video_terminal, fps)
