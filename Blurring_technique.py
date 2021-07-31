import cv2 as cv

img = cv.imread('opencv img.jpg')
cv.imshow('Tree',img)

# Averaging
# In a window say of 3x3 the center pixel's intensity is determined by the average intensity of the surrounding pixels intensity
average = cv.blur(img ,(5,5))
cv.imshow('Average_Tree',average)

# Gaussian Blur
# The surrounding pixels have a specific width assigned and then the center pixel's intensity is given by the average of the surrounding pixels width
gauss = cv.GaussianBlur(img, (5,5), sigmaX=0)
cv.imshow('Gaussian_Tree',gauss)

# Median Blur
# Its the same as Averaging just that here instead of the average, the median is taken
median = cv.medianBlur(img ,5)
cv.imshow('Median_Tree',median)

# Bilateral Blur
# In thi you get to retain the edges of the image as well
bilateral = cv.bilateralFilter(img, 10, sigmaColor=35, sigmaSpace=25)
cv.imshow('Bilaterl_Tree',bilateral)

cv.waitKey(0)