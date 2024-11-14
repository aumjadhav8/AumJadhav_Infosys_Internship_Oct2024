# AI-Enhanced Engagement Tracker for Young Learners (Infosys Internship - October 2024)

## Project Overview

This project implements various computer vision techniques for image processing, video analysis, and face recognition to create an engagement tracking system for young learners. It includes comprehensive implementations for image manipulation, video processing, annotations, and face recognition capabilities.

## Features

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

      
### Video Processing

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84

#### Features:
1. **Multi-video Processing**
   - Batch image processing from folders
   - Dimension analysis and display

2. **Real-time Processing**
   - FPS calculation and display
   - Live video capture and saving
   - Video stacking and concatenation
   - Webcam stream processing

### Annotations

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6

#### Capabilities:
1. **Data Organization**
   - Image and label file segregation
   - Matched/unmatched directory sorting

2. **Label Management**
   - Bounding box visualization
   - Class number updates for object detection

### Face Recognition

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

#### Core Features:
1. **Attendance System**
   - Face recognition implementation
   - Attendance recording and saving
   - Excel sheet integration
   - Date-time tracking

2. **Analysis Tools**
   - Facial landmark detection
   - Attention score calculation
   - Average attention score tracking

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
