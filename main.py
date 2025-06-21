import os

import videodownload

# Remove tmp folder and everything in it
def delete_tmp(output_dir):
    try:
        for filename in os.listdir(output_dir): # deletes files in folder
            os.remove(os.path.join(output_dir, filename))
        os.rmdir(output_dir) # deletes folder now that it is empty
    except FileNotFoundError:
        pass

if __name__ == "__main__":
    output_dir = "./tmp"
    delete_tmp(output_dir) # ensures no additional files affect anything

    yt_url = "https://www.youtube.com/watch?v=FtutLA63Cp8"
    videodownload.video_download(yt_url, output_dir)
