# AI-Enhanced Engagement Tracker for Young Learners (Infosys Internship - October 2024)

## Project Overview

This project implements various computer vision techniques for image processing, video analysis, and face recognition to create an engagement tracking system for young learners. It includes comprehensive implementations for image manipulation, video processing, annotations, and face recognition capabilities.

# Image Processing 📁

This repository contains a collection of Python scripts for various image processing techniques. Each script performs a specific operation that is commonly used in image analysis, ranging from basic transformations to more advanced processing tasks.

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84
- **NumPy**: For array manipulation

### Project Structure

- **`image_processing_techniques`** 🖼️
  
  - **`IMG_Dilation&erosion.py`**
    - This script applies dilation and erosion to images, fundamental morphological operations widely used in image preprocessing.
    - **Output:** ![dialation and erosion](https://github.com/user-attachments/assets/4c83f607-fdfe-4218-89bb-335ea9e87c68)

  - **`IMG_EdgeDetection.py`**
    - Detects edges in images using multiple edge detection algorithms, essential for identifying object boundaries.
    - **Output:** ![edges](https://github.com/user-attachments/assets/7b4bd183-a7b7-427f-ac04-0f96cb156699)


  - **`IMG_GrayscaleNB&Wimg.py`**
    - Converts images to grayscale and black & white, useful for simplifying image data and preprocessing.
    - **Output:** ![Examples](Screenshot 2024-11-13 175547), ![Screenshot](Screenshot 2024-11-13 175613), ![Screenshot](Screenshot 2024-11-13 175603)

  - **`IMG_HSV.py`**
    - Converts images to the HSV (Hue, Saturation, Value) color space, often used in color-based segmentation.
    - **Output:** ![Example](Screenshot 2024-11-13 181524)

  - **`IMG_Multiple_Image_opener.py`**
    - Facilitates opening and processing multiple images simultaneously, useful for batch image processing.
    - **Output:** ![grayscaleimg](https://github.com/user-attachments/assets/bcd88f87-a489-4a65-ad7e-3e0d1e739213)


  - **`IMG_Rotating_img.py`**
    - Rotates images by a specified angle, beneficial for alignment and data augmentation.
    - **Output:** ![rotate](https://github.com/user-attachments/assets/c4ee0205-3a42-4bad-a402-faf77e4834d6)


  - **`IMG_Single_image_opener.py`**
    - Opens and processes a single image, useful for basic image manipulation.
    - **Output:** ![singleimgopener](https://github.com/user-attachments/assets/4e0af3b6-3783-48a2-b8d8-32e7f9c81bf6)


  - **`IMG_blur.py`**
    - Applies blurring techniques to images, often used for noise reduction and smoothing.
    - **Output:** ![Blur](https://github.com/user-attachments/assets/e21aa5c4-5c16-4e1f-8094-2ad4cf0fb060)


  - **`IMG_concatination.py`**
    - Concatenates multiple images into one, useful for creating image mosaics or comparisons.
    - **Output:** ![concatenation](https://github.com/user-attachments/assets/a10eaea9-cc22-4e59-b35f-22436dd8d6d1)


  - **`IMG_contouring.py`**
    - Detects and draws contours around objects in images, suitable for shape analysis and object detection.
    - **Output:** ![contour](https://github.com/user-attachments/assets/52044f4d-0f15-4417-a2ce-98dc734dea79)


  - **`IMG_cropping.py`**
    - Crops images to a specific region, focusing on areas of interest.
    - **Output:** ![cropping](https://github.com/user-attachments/assets/019b6c78-7ff9-462e-9bc3-884f8a1fcb81)


  - **`IMG_hist_eq.py`**
    - Performs histogram equalization to enhance image contrast.
    - **Output:** ![histogrameq](https://github.com/user-attachments/assets/bdbe68ed-1aff-4f02-a6ad-a89fd5fb2aa0)


  - **`IMG_morphological_noise_removal.py`**
    - Removes noise from images using morphological operations, improving quality.
    - **Output:** ![morphnoiseremoval](https://github.com/user-attachments/assets/128bdd95-8f0d-48da-802c-892763aed0fa)


  - **`IMG_resizing_img.py`**
    - Resizes images to specific dimensions, essential for standardizing image sizes.
    - **Output:** ![resize](https://github.com/user-attachments/assets/48a2d5d9-a0c7-460e-adda-93f83e885760)


  - **`IMG_template.py`**
    - A template script providing a basic structure for developing new image processing functions.
    - **Output:** ![template](https://github.com/user-attachments/assets/1714fe6f-4728-4af0-915a-8c603fd4b748)

      
# Video Processing 🎥

This repository contains a collection of Python scripts for various video processing techniques. Each script focuses on a different aspect of video manipulation, from basic recording to real-time streaming and video analysis.

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84

### Project Structure

- **`video_processing_techniques`** 🎥

  - **`Video_recording.py`**
    - Allows recording videos using your webcam or any connected camera. It captures the video feed, processes it, and saves it to the specified file format.
    - **Output:** ![videorecording](https://github.com/user-attachments/assets/5631ac89-4a9d-4bbf-8c2c-e96b3bf2da27)


  - **`Video_stacking.py`**
    - Stacks multiple video streams into a single video frame, displaying them simultaneously in a grid format. Useful for monitoring multiple video feeds in one view.
    - **Output:** ![videostack](https://github.com/user-attachments/assets/404f9df0-69c7-4468-baca-126f93205db9)

  - **`video_Fps_Calculator.py`**
    - Calculates the frames per second (FPS) of a video stream. This script helps in performance analysis by providing real-time FPS data.
    - **Output:** ![videofps](https://github.com/user-attachments/assets/cae71b5d-9502-4eee-8962-cbc5af45501b)

  - **`video_multivideostream.py`**
    - Processes and displays multiple video streams simultaneously. This script is designed to handle multiple video inputs and render them together, allowing for complex video processing and comparison tasks.
    - **Output:** (Visuals not provided)

  - **`video_stream.py`**
    - Streams video from a file or camera in real-time. It serves as a basic utility for video streaming, which can be extended for more advanced processing tasks.
    - **Output:** ![stream](https://github.com/user-attachments/assets/d9bf83af-0f4f-4aef-8da1-b412441fd579)


# Annotations 📝

This folder contains resources for model training and evaluation annotations.

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6


- **gun.jpeg**: A sample image used for testing and demonstration.
  
- **dataset.py**: Script to install necessary packages or dependencies from Kaggle.

- **labelIMG.py**: Used for assigning specific labels or categories to images.

- **label_img_output.txt**: Output file with results generated by `labelIMG.py`.

- **label_manipulation.py**: Script for modifying or updating image labels.

- **segregation.py**: Used for dividing data into specific categories or groups.


# Face Recognition 🧑‍💻

This project leverages Python, OpenCV, dlib, and the face_recognition library to provide functionality for face recognition and attentiveness analysis. The project can detect and log faces, analyze attentiveness based on head pose, and calculate attention scores. Recognized faces and attention metrics are saved with screenshots for further analysis. 

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

## Files 📂

- **attention_score.py**  
  Detects faces, logs attendance with attention scores, and saves screenshots while calculating an average attention score.  
  **Output**:  
 ![attentionscoree](https://github.com/user-attachments/assets/f7b4a615-8c78-45d8-8cf2-37d87a21c1ce)
![attentionscoreexcel](https://github.com/user-attachments/assets/1239d957-56c3-4d23-81ad-5aac3388d898)


- **ave_attention_score.py**  
  Logs attendance and attention scores using facial landmarks to assess attentiveness.  
  **Output**:  
  ![avgattentionscore](https://github.com/user-attachments/assets/77c5b42e-8dbe-47ad-bbcf-a2f8117cc35d)

  ![avgattentionscoreexcel](https://github.com/user-attachments/assets/48d0e61c-3637-4220-94c5-04a8409600ba)


- **excel_sc_dt.py**  
  Captures video, performs face recognition, logs attendance with screenshots every 30 seconds, and tracks attention status.  
  **Output**:  
  ![excelscdt](https://github.com/user-attachments/assets/efb7c4c0-b16d-42a1-b729-0db53a4e555d)


- **excel_sc.py**  
  Similar to `excel_sc_dt.py`, with a different configuration for logging and capturing screenshots.  
  **Output**:  
  ![excelsc](https://github.com/user-attachments/assets/6404fc4a-56f8-4065-83a8-7d2534ebbb99)
  ![excelscexcell](https://github.com/user-attachments/assets/943a6de2-52ec-4197-aa7c-4ceeebda68eb)



- **Face_Recog.py**  
  Basic face detection and recognition using the `face_recognition` library.  
  **Output**:  
  ![facerecog](https://github.com/user-attachments/assets/ad4f20fd-7b32-483e-9be3-1872730b08e2)


- **landmark.py**  
  Uses dlib’s facial landmark predictor to analyze attentiveness based on head pose, logging attention scores and saving annotated screenshots.  
  **Output**:  
  ![landmark](https://github.com/user-attachments/assets/010792ce-3792-4c11-862d-692221e7b2d9)

  ![landmarkss](https://github.com/user-attachments/assets/f1bff5e3-c436-4179-b201-57435c2d267b)


- **text.py**  
  Contains helper functions used across other scripts.  
  **Output**:  
  ![text py](https://github.com/user-attachments/assets/9c62602c-bd21-4cd3-8b7c-5133b641c322)
 
  ![textpyexcel](https://github.com/user-attachments/assets/a3f0e534-615a-4a13-b17a-4b7dae548eee)


- **tools.py**  
  Additional tools and utilities for face recognition and attentiveness analysis.  
  **Output**:  
  ![toolspy](https://github.com/user-attachments/assets/f0dc765b-727a-4c56-b056-5df235e245a9)

  ![toolsexcel](https://github.com/user-attachments/assets/f1bb2fc4-c43b-40c9-9839-3be21ab5fb39)


## Installation

```bash
# Clone the repository
git clone https://github.com/aumjadhav8/AumJadhav_Infosys_Internship_Oct2024.git

# Install required packages
pip install -r requirements.txt
```

## Usage

Each module can be run independently. Here are some example commands:

```python
# For image processing
python image_processing.py --input path/to/image

# For video processing
python video_processing.py --input path/to/video

# For face recognition
python face_recognition.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Aum Jadhav - [GitHub](https://github.com/aumjadhav8)

Project Link: [https://github.com/aumjadhav8/AumJadhav_Infosys_Internship_Oct2024](https://github.com/aumjadhav8/AumJadhav_Infosys_Internship_Oct2024)
