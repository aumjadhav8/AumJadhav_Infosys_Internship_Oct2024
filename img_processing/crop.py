import cv2

img = cv2.imread('images\download.jpeg')
cropped = img[50:200, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
