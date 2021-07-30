import cv2 as cv
import numpy as np

img = cv.imread("opencv img.jpg")
# cv.imshow('Tree',img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> Up
# x --> Right
# y --> left

translated = translate(img,-100,-100)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2 , height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine (img,rotMat,dimensions)

rotated= rotate(img, -45)
cv.imshow("Rotated", rotated)

# Rotate a rotated image
rotated_rotated=rotate(rotated,-45)
cv.imshow("Rotated_Rotated", rotated_rotated)

# Flipping
# 0 -> Flipping image vertically about x-axis
# 1 -> Flipping image horizontally about y-axis
# -1 -> Flipping image vertically as well as horizontally
flip = cv.flip(img,1)
cv.imshow("Flip_vertically", flip)

cv.waitKey(0)