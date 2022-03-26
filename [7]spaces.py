import cv2 as cv
from matplotlib.pyplot import hsv
import matplotlib.pyplot as plt

img = cv.imread('photos/park.jpg')
cv.imshow('park', img)

# plt.imshow(img)
# plt.show()

#Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#HSV
hsved = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsved)

#Lab
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('lab', lab)

#RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsved, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)
# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)