#!usr/bin/env python3
import picamera
from cv2 import *
import numpy as np



#FIRST WE HAVE TO RECORD THE VIDEO
camera = picamera.PiCamera(resolution = ( 320 , 240 ))
stream = picamera.PiCameraCircularIO(camera, seconds = 10)
camera.start_recording(stream, format = 'h264')

#THEN WE HAVE TO SPLIT THE VIDEO IN ITS FRAMES: I want 

video = cv2.VideoCapture(stream)

frames = []
i = 1
frame_name = 'frame' + str(i)
while True:
    ret, frame = cap.read()
    frame_name = frame
    i+=1
    frames.append(frame_name)
    if False:
        i = 1

#OPEN THE FIRST AND SECOND FRAME WITH NUMPY
a = 0
for a in range(len(frames)):
    first_frame = cv2.imread(frame[a], 0) #0 means greyscale
    second_frame = cv2.imread(frame[a+1], 0)
    
    a+=1
    
    
    
