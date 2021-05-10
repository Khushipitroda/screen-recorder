from datetime import datetime

from PIL import ImageGrab
import numpy as np
import cv2
import datetime
# pkg to access windows api
from win32api import GetSystemMetrics

# to capture full screen
width = GetSystemMetrics(0)  # 0 for width
height = GetSystemMetrics(1)  # 1 for height
# provide dynamic file name
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
# for encoding video
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# 1-output name, 2-fourcc (encoding car), 3-framerate, 4-width and height
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

# for webcam 0 for first camera in system

webcam = cv2.VideoCapture(0)
while True:
    # for capturing image make one img var and give some size to it, height width from api (windows)
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    # for creating array of img to give it to open cv
    img_np = np.array(img)
    # img_np won't be in rgb format to set it cvrColor is used
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # for reading from webcam
    _, frame = webcam.read()
    # for frame size
    frame_height, frame_width, _ = frame.shape
    print(frame_height, frame_width)
    # imposing size of frame,overlaying in img_final
    img_final[0:frame_height, 0:frame_width, :] = frame[0:frame_height, 0:frame_width, :]
    # in dialog box of cv to display the area write imshow, first argument will be name of dialog box second is array
    cv2.imshow('screen_recoder', img_final)
    captured_video.write(img_final)
    # for stopping after user press q
    if cv2.waitKey(10) == ord('q'):
        break

# code from programming hero
