from turtle import width
import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Cat', rescaleFrame(img, scale=0.2))

cv.waitKey(0)
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)
    
    cv.imshow('Video', frame)
    cv.imshow("video-resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()