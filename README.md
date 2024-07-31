
# Hand Tracking App

This project is a real-time hand tracking application that utilizes OpenCV, MediaPipe, and Streamlit. The app captures video from the webcam, detects and tracks hand landmarks, and displays the processed video with annotations.

## Features

- **Real-time hand tracking:** Uses MediaPipe's hand tracking solution to detect and track 21 hand landmarks.
- **Visual feedback:** Draws landmarks and connections on the detected hand(s).
- **FPS display:** Shows the current frame rate of the video processing.

## Installation

To run this project, you need to have Python installed along with the following packages:

- OpenCV
- MediaPipe
- Streamlit
- NumPy

You can install these packages using pip:

```bash
pip install opencv-python mediapipe streamlit numpy
```

## Usage

To run the app locally, use the following command:

```bash
streamlit run 3dHand.py
```

## Code Explanation

The core components of the code are:

1. **Importing Libraries:**
   - `cv2`: For video capture and processing.
   - `mediapipe as mp`: For hand tracking.
   - `streamlit as st`: For building the web interface.
   - `numpy as np`: For numerical operations.

2. **Setting Up the Hand Tracking Module:**
   - Initialize MediaPipe Hands solution and drawing utilities.

3. **Main Loop:**
   - Captures frames from the webcam.
   - Processes each frame to detect hands and their landmarks.
   - Draws landmarks and connections on the frame.
   - Displays the processed frame and current FPS on the Streamlit app.

## Notes

- This app requires access to a webcam.
- It is designed for educational and demonstration purposes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
