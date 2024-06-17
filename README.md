# AI-Powered Vehicle Surveillance System

## Overview

Vehicles are an essential part of everyday life for many people. However, vehicle theft remains one of the most challenging and least-solved crimes, requiring significant manual surveillance work. According to a preliminary analysis by the National Insurance Crime Bureau (NICB), vehicle thefts saw a dramatic increase in 2020 compared to 2019, reversing two years of declining thefts. 

Leveraging the maturity and accuracy of Artificial Intelligence (AI) algorithms, this project proposes an AI-powered automated vehicle surveillance system. The system utilizes CCTV cameras to recognize and track vehicles by extracting various attributes such as make, model, color, insurance details, damage, peculiar attachments, license plate number, and type of the plate. A real-time database compiles these details along with date, time, and location stamps, uniquely identifying suspect vehicles involved in criminal activities. These features can also be used as evidence to report violations such as illegal number plates or expired documents. Even if some features of the vehicle are not clearly visible, the system can recognize the vehicle using other features. Based on recently detected locations, the system can track the suspect's route and assist in taking necessary legal actions to prevent and reduce vehicle theft in the future.

## Module Description

### Lane Detection (One-Way, Two-Way Lane)

To perform real-time lane detection in a video, the OpenCV Python library is used. The process includes two steps:

1. **Frame Masking:** Removes unwanted regions or objects from the image or frame.
2. **Image Preprocessing:** Detects lanes in the video frame. This involves:
   - Applying a mask to all frames in the input video.
   - Applying Image Thresholding followed by Hough Line Transformation to detect lane markings.
   
**Image Thresholding:** Assigns pixel values of a grayscale image one of two values (black and white) based on a threshold value. If the pixel value is greater than the threshold, it is assigned one value; otherwise, it is assigned the other value.

**Hough Line Transformation:** Detects shapes that can be mathematically represented, such as rectangles and lines. This technique detects lane markings represented as lines. The main objective is to detect whether a vehicle is moving in the correct lane. The number plates of vehicles not moving in the correct lane are extracted using the YOLO framework.

### Number Plate Detection
**Image Pre-processing**
- **Gray Scaling**: Converts images to grayscale to speed up processing.
- **Edge Detection**: Uses the Canny edge method from OpenCV to detect edges in the image.
- **Contour Detection**: Detects rectangular objects to find the number plate.
- **License Plate Cropping**: Extracts the region of the number plate from the image.
- **Image Processing**: Applies several techniques to reduce noise and emphasize key features of license characters.
- **OCR (Optical Character Recognition)**: Uses Tesseract to extract printed text from images.

**Steps Involved:**
1. **Gray Scaling**
2. **Edge Detection**
3. **Contour Detection**
4. **License Plate Cropping**
5. **Image Processing**:
   - Convert to 255 scale
   - Convert to grayscale
   - Blur image using Gaussian Blur
   - Image thresholding
   - Dilation
6. **OCR**: Extracts characters from the license plate.

**Tech Stack:** OpenCV in Python and YOLO framework.

**YOLO (You Only Look Once) Framework:** Utilized for number plate detection. YOLO is an algorithm that uses neural networks for real-time object detection. It functions by:
- Taking an input image or frame and dividing it into grids.
- Performing image classification and localization on each grid.
- Calculating bounding boxes and their corresponding class probabilities.

## Technologies Used

- **OpenCV:** Used for image and video processing.
- **YOLO Framework:** Used for real-time object detection.
- **Python:** Programming language used for implementation.
- **TensorFlow:** Used for AI and machine learning tasks.

## Benefits to Society

This AI-powered vehicle surveillance system aims to enhance public safety by providing an automated, efficient method for monitoring and tracking vehicles. It helps in:
- Reducing vehicle theft by identifying and tracking suspect vehicles.
- Reporting law violations such as illegal number plates or expired documents.
- Assisting law enforcement agencies in taking necessary actions to prevent crimes.

## Future Scope

As vehicle theft and related crimes continue to evolve, the need for advanced surveillance systems becomes more critical. Future enhancements of this project could include:
- Improved accuracy and speed of detection.
- Integration with other surveillance systems for comprehensive monitoring.
- Expansion to detect other vehicle-related violations and crimes.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- YOLO Framework
- TensorFlow

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Dipika2020/vehicle-surveillance-system.git
   cd vehicle-surveillance-system
