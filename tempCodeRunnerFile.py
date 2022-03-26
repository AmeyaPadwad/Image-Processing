circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('mask', mask)