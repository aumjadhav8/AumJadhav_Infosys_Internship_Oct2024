import cv2
import numpy as np

img1 = cv2.imread("1.jpeg")
img2 = cv2.imread("1.jpeg")
img3 = cv2.imread("1.jpeg")
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))
img3 = cv2.resize(img3, (500, 500))

h_concat = np.hstack((img1, img2))#concatination horizontally adding the two image
v_concat = np.vstack((img1, img2))#concatination vertically adding the two image
img5 = cv2.imread("1.jpeg")
cv2.imshow('Original', img5)
cv2.imshow('Horizontal Concatenation', h_concat)
cv2.imshow('Vertical Concatenation', v_concat)

cv2.waitKey(0)
cv2.destroyAllWindows()