# Eye Blink Counter using OpenCV


## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Screenshots](#screenshots)
- [License](#license)

## Project Overview
The **Eye Blink Counter** is a computer vision application that detects eye blinks in real-time using OpenCV and the cvzone library. By utilizing face mesh detection, it calculates the blink ratio based on the vertical and horizontal distances between key landmarks around the eyes. This application can be useful for monitoring blink frequency, which can be beneficial in various contexts, such as driver alertness, fatigue detection, or even user interaction in gaming.

## Features
- Real-time eye blink detection using a webcam.
- Visualization of eye landmarks for a better understanding of the detection process.
- Blink count displayed on the screen.
- Graphical representation of the blink ratio over time.
- Customizable parameters for different use cases.

## Installation
To run this project, ensure you have Python installed on your system. Follow these steps to set up the project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pahinithi/Eye-Blink-Counter-using-Computer-Vision-OpenCV
   cd Eye-Blink-Counter
   ```

2. **Install the required libraries:**
   ```bash
   pip install opencv-python cvzone
   ```

## Usage
1. Make sure your webcam is connected and working properly.
2. Run the application:
   ```bash
   python main.py
   ```
3. The application will open a window displaying the camera feed with eye blink detection.
4. The blink count will be shown on the screen, and the blink ratio will be plotted in real-time.
5. Press the 'q' key to exit the application.

## Demo

- [Live Demo](https://drive.google.com/file/d/1raJ4x9qa5vphh_SXUzCfI_fHGylOufcA/view?usp=sharing)

## Screenshot

<img width="1728" alt="CV11" src="https://github.com/user-attachments/assets/899547df-9ac3-44d2-ba0c-0a74768ad47b">


## Code Explanation
Here’s a brief explanation of the main components of the code:

- **Camera Initialization:** The code initializes the webcam for capturing video frames.
- **FaceMeshDetector:** A face mesh detector from the cvzone library is utilized to identify facial landmarks.
- **Eye Landmark Points:** The code specifies key landmarks around the eyes using an `idList`.
- **Blink Ratio Calculation:** The vertical and horizontal distances between the landmarks are measured to compute the blink ratio.
- **Blink Detection Logic:** The application counts blinks based on the calculated ratio. A lower ratio indicates a closed eye.
- **Real-Time Visualization:** The application displays the blink count and the current blink ratio graphically.

## License
This project is licensed under the MIT License.

## Contact

For any questions or support, please contact:

- **Name**: Pahirathan Nithilan
- **Email**: [nithilan32@gmail.com](mailto:nithilan32@gmail.com)
- **GitHub**: [Pahinithi](https://github.com/Pahinithi)

