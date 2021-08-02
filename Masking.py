# Masking allows us to focus on a particular part of image that we want to focus on


import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import shape

img = cv.imread('opencv img.jpg')
# cv.imshow('Tree',img)

blank = np.zeros((img.shape[:2]), dtype='uint8')      # The shape of the blank image is supposed to be the same as tht of the image 
# cv.imshow('Blank',blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 - 150,img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle',circle)

rectangle = cv.rectangle(blank.copy(),(150,150),(350,350), 255, -1)
cv.imshow('Rectangle',rectangle)

weird_shape = cv.bitwise_and(circle ,rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shape Masked Image', masked)

cv.waitKey(0)