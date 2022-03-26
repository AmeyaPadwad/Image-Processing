import cv2 as cv
from cv2 import resize

img = cv.imread('photos/park.jpg')
cv.imshow('cat', img)

#converting to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey', grey)

#image blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#edge cascade
edge = cv.Canny(blur, 125, 175)
cv.imshow('edge', edge)

#dilate image
dilate = cv.dilate(edge, (7,7), iterations=2)
cv.imshow('dilated', dilate)

#eroding
erode = cv.erode(dilate, (7,7), iterations=2)
cv.imshow('erode', erode)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resize', resized)

#cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)