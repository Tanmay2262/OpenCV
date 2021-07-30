import cv2 as cv

img = cv.imread("opencv img.jpg") 
cv.imshow("Tree",img)

# Converting to Grayscale
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale Tree', gray)

# Blur an image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur) 

# Edge Cascade
canny = cv.Canny(img ,125,175)
cv.imshow("Canny image",canny)

# Dialating the image
dialated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow("Dilated image",dialated)

# Eroded
eroded = cv.erode(dialated,(3,3), iterations=3)
cv.imshow("Eroded image",eroded)

# Resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized image",resize)

# Cropping
cropped = img[50:200 , 200:400]
cv.imshow("Cropped image",cropped)

cv.waitKey(0)