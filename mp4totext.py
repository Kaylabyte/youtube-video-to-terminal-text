import cv2

import config

def pixel_char(intensity, char_set):
    """Return characters to replace intensity values based on char_set value."""
    if char_set == 1:
        if intensity < 128: return ".."
        else: return "XX"

    elif char_set == 2:
        if intensity < 85: return ".."
        elif intensity < 172: return "**"
        else: return "XX"

    elif char_set == 3:
        if intensity < 85: return "  "
        elif intensity < 172: return "SS"
        else: return "@@"

    elif char_set == 4:
        if intensity < 51: return "  "
        elif intensity < 102: return "░░"
        elif intensity < 155: return "▒▒"
        elif intensity < 206: return "▓▓"
        else: return "██"

    elif char_set == 5:
        if intensity < 51: return "██"
        elif intensity < 102: return "▓▓"
        elif intensity < 155: return "▒▒"
        elif intensity < 206: return "░░"
        else: return "  "

    else:
        return

def frame_draw(frame, height, width, char_set):
    """Draw the frame using the correct character set and return this new frame."""
    frame_text = ""

    for y in range(height): # loops through every pixel for intensity values
        for x in range(width):
            frame_text += pixel_char(frame[y][x], char_set)
        frame_text += "\n"
        
    return frame_text

def frame_area(height, width):
    """Draw an empty frame outlining the display area and return this outline."""
    frame_text = ""

    for y in range(height):
        for x in range(width):
            if y == 0 or y == height - 1: frame_text += "XX"
            elif x == 0 or x == width - 1: frame_text += "XX"
            else: frame_text += "  "
        frame_text += "\n"

    return frame_text

def frame_convert(frame, scale):
    """Scale and convert the frame to greyscale, and return this modified frame alongside its new height and width."""
    frame = cv2.resize(frame, None, fx=scale, fy=scale)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # greyscale, makes working with the frames easier
    
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]

    return frame, frame_height, frame_width

def video_convert(video_mp4, scale, char_set):
    """Convert a video to text and return both the converted video and the FPS."""
    video_capture = cv2.VideoCapture(video_mp4)
    video_terminal = []
    success, frame = video_capture.read()
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    print("Converting video...")

    while success: # loops through every frames
        frame_modified, frame_height, frame_width = frame_convert(frame, scale)
        video_terminal.append(frame_draw(frame_modified, frame_height, frame_width, char_set))
        success, frame = video_capture.read()

    print("Successfully converted video!")

    return video_terminal, fps

def video_info(video_mp4):
    """Display various information about the video."""
    video_capture = cv2.VideoCapture(video_mp4)
    print(f"YouTube URL: {config.YT_URL}")
    print(f"Frame count: {int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))}")
    print(f"FPS: {int(video_capture.get(cv2.CAP_PROP_FPS))}")
    print(f"Width: {int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))}")
    print(f"Height: {int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))}")

if __name__ == "__main__":
    video_capture = cv2.VideoCapture(config.OUTPUT_VIDEO_DIR)

    success, frame = video_capture.read()

    frame_modified, frame_height, frame_width = frame_convert(frame, config.SCALE)
    print(frame_area(frame_height, frame_width))

    print("Please resize the terminal font so the box entirely fits in the screen...")
