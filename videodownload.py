from pytubefix import YouTube

def video_display_info(yt_url):
    """Display the title and all the streams this program may use of the YouTube video."""
    yt = YouTube(yt_url)
    print("Fetching streams...")
    print(yt.title)
    print("\n144p Videos:")
    [print(x) for x in yt.streams.filter(res="144p")]
    print("\nAudio Tracks:")
    [print(x) for x in yt.streams.filter(only_audio=True)]
    print()

def video_download(yt_url, output_dir, output_video, output_audio):
    """Download low quality video and audio from YouTube."""
    yt = YouTube(yt_url)
    print("Downloading video...")
    yt.streams.filter(res="144p", mime_type="video/mp4", only_video=True).first().download(output_path=output_dir, filename=output_video)
    yt.streams.filter(mime_type="audio/mp4", only_audio=True).first().download(output_path=output_dir, filename=output_audio)
    print("Successfully downloaded video!")

if __name__ == "__main__":
    import config

    video_display_info(config.YT_URL)
    video_download(config.YT_URL, config.OUTPUT_DIR, config.OUTPUT_VIDEO_NAME, config.OUTPUT_AUDIO_NAME)

    print("Tasks complete!!!")
