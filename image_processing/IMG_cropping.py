import cv2

img = cv2.imread("1.jpeg")
cropped = img[50:200, 100:300]#roi-region of insterest ;cropped = img[start_y:end_y, start_x:end_x]
img1 = cv2.imread("1.jpeg")
cv2.imshow('Original', img1)
cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
