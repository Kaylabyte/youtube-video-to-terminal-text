import os

import config
import videodownload
import mp4totext
import playtextvideo

def delete_output(output_dir):
    """Delete everything in the output folder."""
    for file_name in os.listdir(output_dir):
        os.remove(os.path.join(output_dir, file_name))

if __name__ == "__main__":
    if config.YT_DOWNLOAD:
        delete_output(config.OUTPUT_DIR) # ensures no additional files will affect anything
        videodownload.video_download(config.YT_URL, config.OUTPUT_DIR, config.OUTPUT_VIDEO_NAME, config.OUTPUT_AUDIO_NAME)

    video_terminal, fps = mp4totext.video_convert(config.OUTPUT_VIDEO_DIR, config.SCALE, config.CHAR_SET)
    playtextvideo.play_video(config.OUTPUT_AUDIO_DIR, video_terminal, fps)
