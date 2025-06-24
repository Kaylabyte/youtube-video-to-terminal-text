import cv2

def frame_save(frame, count, scale):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(frame, None, fx=scale, fy=scale)
    cv2.imwrite(f"./tmp/testframes/frame{count + 1}.jpg", resized_frame)

def video_info(ytvideo):
    print(f"Frame count: {int(ytvideo.get(cv2.CAP_PROP_FRAME_COUNT))}")
    print(f"FPS: {int(ytvideo.get(cv2.CAP_PROP_FPS))}")
    print(f"Width: {int(ytvideo.get(cv2.CAP_PROP_FRAME_WIDTH))}")
    print(f"Height: {int(ytvideo.get(cv2.CAP_PROP_FRAME_HEIGHT))}")


if __name__ == "__main__": # for me :D
    import os # ehhhhhhhhhhhhhh
    import main # I'm lazy
    
    ytvideo = cv2.VideoCapture("./tmp/video.mp4")
    scale = 0.5

    # Lazily cleans out testframes folder
    main.delete_tmp("./tmp/testframes")
    try:
        os.mkdir("./tmp/testframes")
    except FileExistsError:
        pass

    video_info(ytvideo)

    success, frame = ytvideo.read()
    count = 0
    while success: # loops through all the frames
        frame_save(frame, count, scale)
        success, frame = ytvideo.read()
        count += 1
    else:
        print("Finished saving frames!!!")
