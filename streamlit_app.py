import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function: get color mask
def get_color_mask(frame, color_ranges):
    if frame is None or frame.size == 0:
        raise ValueError("Invalid input frame.")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    masks = []
    for lower, upper, color_name in color_ranges:
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        masks.append((mask, color_name))
    return masks

# Function: detect colors
def detect_colors(frame, color_ranges):
    if frame is None or frame.size == 0:
        raise ValueError("Invalid input frame.")
    result = frame.copy()
    masks = get_color_mask(frame, color_ranges)
    for mask, color_name in masks:
        contours_info = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours_info[-2]  # works for both OpenCV 3 & 4
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # filter small objects
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(result, (x, y), (x+w, y+h), (0, 255, 0), 2)
                text_y = y - 10 if y - 10 > 20 else y + 20
                cv2.putText(result, color_name, (x, text_y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    return result

# ---------------- Streamlit App ----------------
st.title("🎨 Color Detection App")

# Define HSV color ranges
color_ranges = [
    ((0, 120, 70), (10, 255, 255), "Red"),
    ((170, 120, 70), (180, 255, 255), "Red"),
    ((36, 50, 70), (89, 255, 255), "Green"),
    ((90, 50, 70), (128, 255, 255), "Blue"),
    ((20, 100, 100), (30, 255, 255), "Yellow"),
    ((10, 100, 20), (25, 255, 255), "Orange"),
    ((129, 50, 70), (158, 255, 255), "Purple")
]

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read image
    image = Image.open(uploaded_file)
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Detect colors
    output = detect_colors(frame, color_ranges)

    # Convert back to RGB for Streamlit
    output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

    st.image(output_rgb, caption="Detected Colors", use_column_width=True)
