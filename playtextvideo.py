import os
import time
import multiprocessing

from pydub import AudioSegment
from pydub.playback import play

def play_audio(audio_m4a):
    """Play the audio, pretty self explanatory function."""
    audio_segment = AudioSegment.from_file(audio_m4a)
    play(audio_segment)

def next_frame(frame):
    """Clear the screen and display the next frame."""
    print("\033c", end="") # ANSI escape sequence
    print(frame)

def playback_frame_sched(delay, video_terminal):
    """Time the playback speed to match the FPS with no drift."""
    next_time = time.time() + delay

    for frame in video_terminal:
        time.sleep(max(0, next_time - time.time()))
        next_frame(frame)
        next_time += delay

def play_video(audio_m4a, video_terminal, fps):
    """Play the audio and video at the same time in separate processes."""
    if not os.path.exists(audio_m4a):
        print("Audio file not found. No audio will be played...")
    elif os.path.getsize(audio_m4a) <= 0:
        print("Audio file appears to be corrupted. No audio will be played...")
    if len(video_terminal) == 0:
        raise Exception(
            "Video failed to play.\nIf this happens again, please send me the video URL so I can "
            "figure out the issue."
        )

    time.sleep(3)

    try:
        process_audio = multiprocessing.Process(target=play_audio, args=(audio_m4a,))
        process_video = multiprocessing.Process(target=playback_frame_sched, args=(1/fps, video_terminal))

        process_audio.start()
        process_video.start()

        process_audio.join()
        process_video.join()
    except KeyboardInterrupt:
        print("\nPlayback interrupted...")
        raise SystemExit

    print("Finished video...")
        
if __name__ == "__main__":
    import config
    import mp4totext

    mp4totext.video_info(config.OUTPUT_VIDEO_DIR)
    print("Please run main.py to start this program...")

