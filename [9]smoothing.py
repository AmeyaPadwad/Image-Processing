import cv2 as cv
from numpy import average

img = cv.imread('photos/cats.jpg')
cv.imshow('cats', img)

#averaging
averaged = cv.blur(img, (7,7))
cv.imshow('average', averaged)

#gaussian_blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian', gaussian)

#median
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

#bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)