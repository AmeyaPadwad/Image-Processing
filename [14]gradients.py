import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap', lap)

#sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel', sobel)

#canny
canny = cv.Canny(gray, 125, 175)
cv.imshow('canny', canny)

cv.waitKey(0)