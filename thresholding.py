# Thresholding is basically the binarisation of the image.
# i.e. where the pixels of the image are either 0, 255 or 1.
import cv2 as cv
import numpy as np

img = cv.imread('opencv img.jpg')
# cv.imshow('Tree',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)    # 100 ->255
# cv.imshow("Threshod_tree", thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
# cv.imshow("Threshod_inv_tree", thresh_inv)

# Adaptive Threshold
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("adaptiveThreshold_tree", adaptive_thresh)


cv.waitKey(0)