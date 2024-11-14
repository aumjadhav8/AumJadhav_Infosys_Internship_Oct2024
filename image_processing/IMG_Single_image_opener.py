

import cv2 # type: ignore #type ignore this

# Read an image
image = cv2.imread("1.jpeg")

# Display the image using OpenCV
print(image.shape)
cv2.imshow('Image 3', image)#cv2.imshow() function is used to display it in a window named "Image"
cv2.waitKey(0)#cv2.waitKey(0) function waits for a key press before closing the window, allowing the user to view the image.
cv2.destroyAllWindows()# cv2.destroyAllWindows() closes all open windows
# To check dimensions of the image
print(image.shape) #The image.shape attribute is used to print the dimensions of the image, which will be in the format (height, width, channels).


'''import cv2 # type: ignore

# Read an image
image = cv2.imread(" ")

if image is None:
    print("Error: Could not read the image.")
else:
    # Display the image using OpenCV
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # To check dimensions of the image
    print(image.shape)'''