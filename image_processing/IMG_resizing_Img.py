import cv2

img = cv2.imread("1.jpeg")
img1 = cv2.imread('1.jpeg')
resized = cv2.resize(img, (300, 300))
cv2.imshow('Original', img1)
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
