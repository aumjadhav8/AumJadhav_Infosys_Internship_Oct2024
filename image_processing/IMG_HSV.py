import cv2

img = cv2.imread("1.jpeg")
img1 = cv2.imread('1.jpeg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Original', img1)
cv2.imshow('HSV Image', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()