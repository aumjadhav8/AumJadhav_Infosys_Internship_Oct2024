import cv2

# Load the original image in grayscale
img = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE)
# Load the template image in grayscale
template = cv2.imread("1.jpeg", cv2.IMREAD_GRAYSCALE)

# Ensure both images are loaded properly
if img is None or template is None:
    print("Error loading image or template")
else:
    # Check if the template is larger than the image
    if template.shape[0] > img.shape[0] or template.shape[1] > img.shape[1]:
        print("Template size is larger than the source image. Please use a smaller template.")
    else:
        # Perform template matching
        result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        # Get the dimensions of the template
        h, w = template.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        
        # Draw a rectangle around the matched region
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        
        # Display the result
        cv2.imshow('Detected Template', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
