import cv2
import os

folder_path = "C:\\Users\\Acer\\Videos\\Screen Recordings"

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    # Check if the file is a video
    if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
        cap = cv2.VideoCapture(file_path)
        
        if not cap.isOpened():
            print(f"Failed to open video {filename}")
            continue
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('Video', frame)
            
            # Press 'q' to exit the video early and move to the next one
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()  # Release the video capture object
        cv2.destroyAllWindows()  # Close the video window
        print(f"Finished playing {filename}")
    else:
        print(f"{filename} is not a video file")
