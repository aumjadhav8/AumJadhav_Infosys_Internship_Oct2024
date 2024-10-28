import cv2

cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()  # Terminate the program if the webcam can't be accessed

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()  

    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

# Close all the OpenCV windows
cv2.destroyAllWindows()
