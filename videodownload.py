import pytubefix
from pytubefix import YouTube

def video_display_info(yt_url):
    """Display the title and all the streams this program may use of the YouTube video."""
    try:
        yt = YouTube(yt_url)
        print("Fetching streams...")
        print(yt.title)
        print("\n144p Videos:")
        [print(x) for x in yt.streams.filter(res="144p")]
        print("\nAudio Tracks:")
        [print(x) for x in yt.streams.filter(only_audio=True)]
        print()
    except pytubefix.exceptions.VideoUnavailable as error:
        raise pytubefix.exceptions.PytubeFixError(
            "Video unavailable. The video may be unlisted, private, or region-locked.\nPlease provide "
            "a different video to YT_URL (in the \"config.py\" file), then try again..."
        ) from error
    except pytubefix.exceptions.RegexMatchError as error:
        raise pytubefix.exceptions.PytubeFixError(
            "Video not found.\nPlease ensure the URL provided in YT_URL (in the \"config.py\" file) "
            "is a valid YouTube link, then try again..."
        ) from error

def video_download(yt_url, output_dir, output_video, output_audio):
    """Download low quality video and audio from YouTube."""
    try:
        print("Downloading video...")
        yt = YouTube(yt_url)

        stream_video = yt.streams.filter(res="144p", mime_type="video/mp4", only_video=True).first()
        if stream_video is None:
            raise pytubefix.exceptions.PytubeFixError(
                "No video streams were found.\nIf this happens again, please send me the video URL "
                "so I can figure out the issue."
            )

        stream_audio = yt.streams.filter(mime_type="audio/mp4", only_audio=True).first()
        if stream_audio is None:
            raise pytubefix.exceptions.PytubeFixError(
                "No audio streams were found.\nIf this happens again, please send me the video URL "
                "so I can figure out the issue."
            )

        stream_video.download(output_path=output_dir, filename=output_video)
        stream_audio.download(output_path=output_dir, filename=output_audio)

        print("Successfully downloaded video!")
    except pytubefix.exceptions.VideoUnavailable as error:
        raise pytubefix.exceptions.PytubeFixError(
            "Video unavailable. The video may be unlisted, private, or region-locked.\nPlease provide "
            "a different video to YT_URL (in the \"config.py\" file), then try again..."
        ) from error
    except pytubefix.exceptions.RegexMatchError as error:
        raise pytubefix.exceptions.PytubeFixError(
            "Video not found.\nPlease ensure the URL provided in YT_URL (in the \"config.py\" file) "
            "is a valid YouTube link, then try again..."
        ) from error

if __name__ == "__main__":
    import config

    video_display_info(config.YT_URL)
    video_download(config.YT_URL, config.OUTPUT_DIR, config.OUTPUT_NAME_VIDEO, config.OUTPUT_NAME_AUDIO)

    print("Tasks complete!!!")
