import cv2 as cv
from cv2 import circle
from cv2 import rectangle
import numpy as np

img = cv.imread('photos/cats 2.jpg')
cv.imshow('cats2', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

mask = cv.bitwise_xor(rectangle, circle)
cv.imshow('mask', mask)

masked_img = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked_img)

cv.waitKey(0)