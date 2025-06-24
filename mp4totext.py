import cv2

def frame_convert(frame, scale, char_full, char_empty, char_middle):
    frame = cv2.resize(frame, None, fx=scale, fy=scale)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # greyscale, makes working with the frames easier
    
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    frame_text = ""

    # Loops through every pixel for their colour values
    for y in range(frame_height):
        for x in range(frame_width):
            pixel = frame[y][x]
            # if pixel < 128: frame_text += char_empty
            # else: frame_text += char_full
            if pixel < 85: frame_text += char_empty
            elif pixel < 171: frame_text += char_middle
            else: frame_text += char_full
        frame_text += "\n"
        
    return frame_text

def video_convert(video_mp4, scale, char_full, char_empty, char_middle):
    video_capture = cv2.VideoCapture(video_mp4)
    video_terminal = []
    success, frame = video_capture.read()
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    print("Converting Video...")

    while success: # loops through all the frames
        video_terminal.append(frame_convert(frame, scale, char_full, char_empty, char_middle))
        success, frame = video_capture.read()

    return video_terminal, fps

def video_info(video_capture):
    print(f"Frame count: {int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))}")
    print(f"FPS: {int(video_capture.get(cv2.CAP_PROP_FPS))}")
    print(f"Width: {int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))}")
    print(f"Height: {int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))}")

if __name__ == "__main__": # for me :D
    video_capture = cv2.VideoCapture("./tmp/video.mp4")
    scale = 0.5
    char_full = "XX"
    char_empty = ".."

    video_info(video_capture)

    for x in range(100): # I don't wanna test on a completely black frame :|
        success, frame = video_capture.read()

    terminal_frame = frame_convert(frame, scale, char_full, char_empty)
    print(terminal_frame)
