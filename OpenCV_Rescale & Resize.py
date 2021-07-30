import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

#read the image
img=cv.imread("opencv img.jpg")

#read the video
vid=cv.VideoCapture("opencv vid.mp4")

def rescaleFrame(frame,scale=2.00):
#    works for images, videos and live videos     
    width = int(frame.shape[1]* scale)
    height = int(frame.shape[0] * scale)
    dimensions= (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#for images
cv.imshow("tree",img)
resized_tree=rescaleFrame(img,0.5)
cv.imshow("tree_resized",resized_tree)
cv.waitKey(0)

#for videos
while True:
  success,frame=vid.read() 

  frame_resized=rescaleFrame(frame)
  
  cv.imshow("waterfall",frame)
  cv.imshow("waterfall_resized",frame_resized)

  if cv.waitKey(20) & 0xFF==ord('q'):
    break

vid.release()
cv.destroyAllWindows

def changeRes(width,height):
   #only for live video
    vid.set(3,width)
    vid.set(4,height)