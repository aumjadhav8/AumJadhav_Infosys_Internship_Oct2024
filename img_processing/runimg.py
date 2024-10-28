import cv2

# Read an image
image = cv2.imread('images\download.jpeg')

# Display the image using OpenCV
cv2.imshow('images\download.jpeg', image)

cv2.waitKey(2000)
cv2.destroyAllWindows()

# To check dimensions of the image
print(image.shape)




