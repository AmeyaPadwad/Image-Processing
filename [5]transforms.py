import cv2 as cv
import numpy as np

img = cv.imread('photos/park.jpg')

cv.imshow('park', img)

#translation
#x and y are no. of pixels to be shifted
def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimens = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimens)

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None :
        rotPoint = (width
        //2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimens = (width, height)

    return cv.warpAffine(img, rotMat, dimens)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

#resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#flipping
#0=flip vertically, 1=flip horizontally, -1=flip both v and h
flipped = cv.flip(img, -1)
cv.imshow('flipped', flipped)

#cropping
cropped = img[200:300, 300:500]
cv.imshow('crop', cropped)

cv.waitKey(0)