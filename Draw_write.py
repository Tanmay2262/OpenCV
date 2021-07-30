# Importing Libraries
import numpy as np
import cv2 as cv

# Creating a blank image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow("blank",blank)

#1. Paint the image with a certain color
#blank[200:300, 300:400]=255,0,0

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)    #thickness=cv.Filled or thickness=-1

# 3.Draw a Circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),radius=50,color=(0,0,255),thickness=-1)

# 4.Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), color=(255,0,0), thickness=3)

# 5.Put text on an image
cv.putText(blank, "First OpenCV Trail", (100,350), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255))
cv.imshow("Text",blank)

cv.waitKey(0)