# Generally there are 3 color channels B->Blue, R->Red and G->Green
# so OpenCV allows you to split the image into their respective color component

import cv2 as cv
import numpy as np

img = cv.imread('opencv img.jpg')
cv.imshow('Tree',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)       #splits the image into blu, green and red

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

# In the output where it is dark there they have lower concentration of those particular colors
# And where it is light it has higher concentration of that particular color

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# (539, 960, 3) represents the shape of the image where 3 is the no. of color channels  

merged=cv.merge([b,g,r])
cv.imshow('BGR_tree',merged)

cv.waitKey(0)