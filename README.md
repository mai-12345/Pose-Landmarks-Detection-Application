# Pose Landmarks Detection Application

This is a Streamlit-based application for detecting pose landmarks in uploaded images using MediaPipe. The application detects human body pose landmarks such as head, shoulders, elbows, wrists, hips, knees, and ankles, and visualizes these landmarks on the input image.

## Features

- Upload an image in `.png`, `.jpg`, `.jpeg`, `.webp`, or `.avif` format.
- Detect and visualize pose landmarks.
- The application uses MediaPipe's Pose Landmarker for real-time landmark detection.

## Requirements

To run the Pose Landmarks Detection Application, you'll need Python 3.x and the following libraries:

1. **Streamlit**: For creating the web interface.
2. **OpenCV**: For handling image processing.
3. **NumPy**: For array manipulation.
4. **MediaPipe**: For pose detection and landmark visualization.
5. **Pillow (PIL)**: For image handling.

### Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run Pose_Landmarks_Detection.py
    ```

4. The application will open in your web browser. You can upload an image to detect pose landmarks.

## How It Works

1. **Image Upload**: Users can upload images via the Streamlit interface.
2. **Pose Landmark Detection**: The image is processed using MediaPipe's PoseLandmarker, which detects various pose landmarks.
3. **Visualization**: The detected landmarks are drawn on the image and displayed to the user.

## Acknowledgments

This project uses **MediaPipe** for pose detection and **Streamlit** for the web interface. Special thanks to the authors of these libraries for their contributions.

