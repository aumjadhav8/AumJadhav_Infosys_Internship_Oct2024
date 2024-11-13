# AI-Enhanced Engagement Tracker for Young Learners (Infosys Internship - October 2024)

## Project Overview

This project implements various computer vision techniques for image processing, video analysis, and face recognition to create an engagement tracking system for young learners. It includes comprehensive implementations for image manipulation, video processing, annotations, and face recognition capabilities.

## Features

### Image Processing

#### Libraries Used:
- **OpenCV**: Version 4.10.0.84
- **NumPy**: For array manipulation

#### Key Functionalities:

1. **Image Concatenation**
   - Resizes and combines images both horizontally and vertically
   - Supports custom pixel range specifications

2. **Contour Detection**
   - Implements grayscale to binary threshold conversion
   - Detects and draws contours in green

3. **Image Enhancement**
   - Cropping with pixel-range specification
   - Dilation and erosion operations
   - Edge detection using Canny algorithm
   - Histogram equalization
   - Color space conversion (BGR to HSV)

4. **Image Transformations**
   - Morphological operations (opening and closing)
   - Image resizing
   - Color to grayscale conversion
   - 90-degree rotation
   - Gaussian blur implementation
   - Noise removal and gap filling
   - Template matching

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
