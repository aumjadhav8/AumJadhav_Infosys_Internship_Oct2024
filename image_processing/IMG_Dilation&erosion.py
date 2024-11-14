import cv2
import numpy as np

img = cv2.imread('1.jpeg', 0)
img1 = cv2.imread('1.jpeg')
kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=1)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('Original', img1)
cv2.imshow('Dilated Image', dilation)
cv2.imshow('Eroded Image', erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
