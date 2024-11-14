import cv2# type: ignore

cap = cv2.VideoCapture(2)# index number of camera to capture

if not cap.isOpened():
    print("Error: Could not open the video camera.")
    exit()

while True:
    ret, frame = cap.read()# help run 
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()