import cv2 # type: ignore

# Load the image
image = cv2.imread("1.jpeg")  # Replace "your_image.jpg" with your actual image path

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to create a black and white image 
_, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the original and converted images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.imshow("Black and White Image (Thresholded)", thresh_image)

# Wait for key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()