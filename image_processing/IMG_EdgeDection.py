import cv2

img = cv2.imread('1.jpeg', 0)
img1 = cv2.imread('1.jpeg')
edges = cv2.Canny(img, 100, 200)
cv2.imshow('Original', img1)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()