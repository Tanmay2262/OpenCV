

import cv2 as cv
import numpy as np

img = cv.imread('opencv img.jpg')
cv.imshow('Tree',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_tree', gray)

# Laplacian Method
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

# Sobel
soeblx = cv.Sobel(gray, cv.CV_64F, 1, 0)
soebly = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobel X", soeblx)
cv.imshow("Sobel Y", soebly)

combined_sobel = cv.bitwise_or(soeblx, soebly)
cv.imshow("Combined_Sobel", combined_sobel)

# Canny (for comparison)
canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny", canny)


cv.waitKey(0)