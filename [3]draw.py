from tokenize import blank_re
import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')

cv.imshow('blank', blank)

blank[200:300, 300:400] = 0,255,0

cv.imshow('green', blank)

cv.rectangle(blank, (0,0), (blank.shape[0],blank.shape[1]), (255,255,255), thickness=-1)

cv.imshow('rec', blank)

cv.circle(blank, (250,250), 40, (255,0,0), -1)

cv.imshow('rec', blank)

cv.line(blank, (0,0), (250,250), (0,255,0), 2)

cv.imshow('rec', blank)

cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0,0,255), 5)

cv.imshow('rec', blank)

cv.waitKey(0)