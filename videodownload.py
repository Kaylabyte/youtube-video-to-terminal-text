from pytubefix import YouTube

# Display video title and streams - FOR TESTING
def video_display_info(yt_url):
    yt = YouTube(yt_url)
    print(yt.title)
    print("\nLOW RESOLUTION:")
    [print(x) for x in yt.streams.filter(res="144p")]
    print("\nAUDIO TRACKS:")
    [print(x) for x in yt.streams.filter(only_audio=True)]

# Download low quality video and audio
def video_download(yt_url, output_dir, output_video, output_audio):
    yt = YouTube(yt_url)
    print("Downloading Video...")
    yt.streams.filter(res="144p", mime_type="video/mp4", only_video=True).first().download(output_path=output_dir, filename=output_video)
    yt.streams.filter(mime_type="audio/mp4", only_audio=True).first().download(output_path=output_dir, filename=output_audio)

if __name__ == "__main__": # for me :D
    yt_url = "https://www.youtube.com/watch?v=FtutLA63Cp8"
    test_streams = input("Test streams? [y/N]: ")
    test_download = input("Test download? [y/N]:")

    if test_streams == "y":
        video_display_info(yt_url)

    if test_download == "y":
        output_dir = "testing_folder"
        video_download(yt_url, output_dir)

    print("Test(s) complete!")
