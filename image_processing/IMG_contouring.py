import cv2
img1 = cv2.imread("1.jpeg")
img = cv2.imread("1.jpeg",0)
_, threshold = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) #255 =white ,>127 is black 
contours ,_= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0, 256, 0), 0)
cv2.imshow('Original', img1)
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()