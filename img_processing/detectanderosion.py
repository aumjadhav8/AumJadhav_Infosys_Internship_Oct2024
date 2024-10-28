import cv2
import numpy as np

img = cv2.imread('images\download.jpeg', 0)

kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=2)

erosion = cv2.erode(img, kernel, iterations=2)

cv2.imshow('Dilated Image', dilation)

cv2.imshow('Eroded Image', erosion)

cv2.waitKey(0)

cv2.destroyAllWindows()
