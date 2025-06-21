import os

from pytubefix import YouTube

# Remove tmp folder and everything in it
def delete_tmp():
    try:
        for filename in os.listdir("./tmp"): # deletes files in folder
            os.remove(os.path.join("./tmp", filename))
        os.rmdir("./tmp") # deletes folder now that it is empty
    except FileNotFoundError:
        pass

# Display video title and streams - FOR TESTING
def video_display_info(yt):
    print(yt.title)
    print("\nLOW RESOLUTION:")
    [print(x) for x in yt.streams.filter(res="144p")]
    print("\nAUDIO TRACKS:")
    [print(x) for x in yt.streams.filter(only_audio=True)]

# Download low quality video and audio
def video_download(yt):
    print("Downloading Video...")
    yt.streams.filter(res="144p", mime_type="video/mp4", only_video=True).first().download(output_path="./tmp", filename="video.mp4")
    yt.streams.filter(mime_type="audio/mp4", only_audio=True).first().download(output_path="./tmp", filename="audio.m4a")

delete_tmp() # ensures no additional files affect anything
yt = YouTube("https://www.youtube.com/watch?v=FtutLA63Cp8")
video_display_info(yt)
video_download(yt)
