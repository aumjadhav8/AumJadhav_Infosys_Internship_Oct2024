import cv2  
cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("Error: Could not open the video camera.")
    exit()

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('saved\output.avi', fourcc, 20.0, (640, 480))


while True:
    ret, frame = cap.read()  # Capture a frame from the webcam
    if not ret:
        # If the frame was not captured successfully, print an error and break the loop
        print("Error: Failed to capture frame.")
        break

    out.write(frame)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the video capture object to free up the webcam
out.release()  # Release the video writer object to save and close the output file

# Destroy all OpenCV windows to clean up
cv2.destroyAllWindows()
