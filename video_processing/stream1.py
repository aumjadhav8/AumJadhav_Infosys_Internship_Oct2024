import cv2

cap = cv2.VideoCapture('Random.mp4') 

if not cap.isOpened():           
    print("Error: Could not open the video camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
