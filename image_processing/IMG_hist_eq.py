import cv2

img = cv2.imread("1.jpeg",0)
equalized = cv2.equalizeHist(img)

img1 = cv2.imread('1.jpeg')
cv2.imshow('Original', img1)
cv2.imshow('Equalized Image', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()