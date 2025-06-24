import os
import time
import multiprocessing

from pydub import AudioSegment
from pydub.playback import play

def play_audio(audio_m4a):
    audio_segment = AudioSegment.from_file(audio_m4a)
    play(audio_segment)

def next_frame(frame):
    os.system("clear")
    print(frame)

# Timer that hopefully avoids drift
def task_sched(delay, video_terminal):
    next_time = time.time() + delay

    for frame in video_terminal:
        time.sleep(max(0, next_time - time.time()))
        next_frame(frame)
        next_time += delay

def play_video(audio_m4a, video_terminal, fps):
    process_audio = multiprocessing.Process(target=play_audio, args=(audio_m4a, ))
    process_video = multiprocessing.Process(target=task_sched, args=(1/fps, video_terminal))

    process_audio.start()
    process_video.start()

    process_audio.join()
    process_video.join()

    print("Finished Video...")
        
if __name__ == "__main__":
    video_terminal = []
    fps = 30
    audio_m4a = "./tmp/audio.m4a"

    # with open("./tmp/hahafunky.txt", "r") as file:
    #     count = 0
    #     video_frame = ""
    #     for line in file:
    #         video_frame += line 
    #         count += 1
    #         if count == 72:
    #             video_terminal.append(video_frame)
    #             count = 0
    #             video_frame = ""

    play_video(audio_m4a, video_terminal, fps)

