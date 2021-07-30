# contours are basically the outline of objects,
# the line or curves that joins the continuous points along the boundry of an object

import cv2 as cv
import numpy as np

img = cv.imread("opencv img.jpg") 
# cv.imshow('Tree',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur_Tree',blur)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale_Tree',gray)

canny= cv.Canny(gray,125,175)
cv.imshow('Canny_Tree',canny)

# Threshold method binarizes the image i.e. 1 -> white & 0 -> black

# ret, thresh= cv.threshold(gray,125,225, cv.THRESH_BINARY)
# cv.imshow('Thresh_Tree',thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# contours ->  a python list of all the coordinates of the contours that were found in the image,
# hierarchies -> refers to the hierarchical representation of contours  
# RETR_LIST -> returns all the contours found in the image 
# RETR_EXTERNAL -> returns only the external contours
# RETR_TREE -> returns all the hierarchical contours
print(f'{len(contours)} contour(s) found' )

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)