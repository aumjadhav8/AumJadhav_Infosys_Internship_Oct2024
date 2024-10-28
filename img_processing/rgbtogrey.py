import cv2

image = cv2.imread("images\img.jpeg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite("images\img.jpeg", gray_image)

cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()
