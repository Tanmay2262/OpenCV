# Color Spaces are basically a space of colors
# OR 
# Color Spaces is system representing an array of colors
# Eg. RBG, GrayScale, HSV, etc.


# OpenCV displays only BGR image while matplotlib.pyplot displays a RBG image

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('opencv img.jpg')
cv.imshow('Tree',img)

# plt.imshow(img)
# plt.show()

# BGR to GrayScale
# Grayscale usually show the pixel intensity at a particular area in an image
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray_Tree',gray)

# BGR to HSV (Hue Saturation Value)
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV_Tree',hsv)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB) 
# cv.imshow('LAB_Tree',lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('RGB_Tree',rgb)

# plt.imshow(rgb)
# plt.show()            # Give the BGR image

# HSV to BGR
nor_half = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('Normal_half_Tree',nor_half) 

nor_full = cv.cvtColor(nor_half,cv.COLOR_BGR2GRAY)
cv.imshow('Normal_full_Tree',nor_full) 

cv.waitKey(0)
