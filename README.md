# 🎨 Colour Detection using OpenCV & Streamlit

This is a **Color Detection Application** built for a hackathon, using **OpenCV, NumPy, Pandas, and Streamlit**. It detects colors in images, videos, or real-time webcam feeds, highlighting them with bounding boxes and providing detailed outputs.

---

## 🚀 Features
- **Multiple Color Detection**: Identifies Red, Green, Blue, Yellow, Orange, and Purple in images, videos, or webcam feeds.
- **Bounding Boxes & Labels**: Draws bounding boxes around detected regions with color names and RGB values.
- **Expanded Color Support**: Added Yellow, Orange, and Purple to the original Red, Green, Blue palette (Level 2 enhancement).
- **Enhanced Debug Tools**: 
  - Toggle debug mode to visualize individual HSV masks for each color.
  - Display a combined HSV mask for all detected colors.
- **Real-Time Processing**: Supports real-time color detection via webcam.
- **Data Export**: Exports detection results (color names, RGB values, bounding box coordinates) as a Pandas DataFrame and CSV.
- **User-Friendly Interface**: Streamlit-based UI for uploading media and toggling debug options.

---

## 🛠️ Tech Stack
- **Python**: Core language for implementation.
- **OpenCV**: Handles image/video processing and color detection.
- **NumPy**: Manages array operations for HSV ranges and masks.
- **Pandas**: Organizes detection results for export.
- **Streamlit**: Provides an interactive web interface.

---

## 📂 Project Structure
- `app.py`: Main Streamlit script for the user interface.
- `utils.py`: Utility functions for color detection and processing.
- `requirements.txt`: List of project dependencies.
- `README.md`: Project documentation.
- `assets/`: Folder for sample images/videos.
  - `sample_image.jpg`: Sample image for testing.
  - `sample_video.mp4`: Sample video for testing.
- `output/`: Folder for saving processed results (images, videos, CSVs).

---

## 📋 Prerequisites
- Python 3.8 or higher.
- Webcam (for real-time detection).
- Basic knowledge of HSV color space for tuning ranges.

---

## 🛠️ Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/colour-detection.git
   cd colour-detection
