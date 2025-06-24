import os

import videodownload
import mp4totext

# Remove tmp folder and everything in it
def delete_tmp(output_dir):
    try:
        for filename in os.listdir(output_dir): # deletes files in folder
            os.remove(os.path.join(output_dir, filename))
        os.rmdir(output_dir) # deletes folder now that it is empty
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    output_dir = "./tmp/"
    yt_url = "https://www.youtube.com/watch?v=FtutLA63Cp8"
    output_video = "video.mp4"
    output_audio = "audio.m4a"
    scale = 0.5
    char_full = "XX"
    char_empty = ".."

    delete_tmp(output_dir) # ensures no additional files affect anything
    videodownload.video_download(yt_url, output_dir, output_video, output_audio)
    video_terminal = mp4totext.video_convert(output_dir + output_video, scale, char_full, char_empty)

