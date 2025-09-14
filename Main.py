import cv2
import numpy as np
from utils import detect_colors

def main():
    # Define HSV ranges for colors (including future enhancement)
    color_ranges = [
        # Existing colors (example)
        ((0, 100, 100), (10, 255, 255), "Red"),
        ((110, 100, 100), (130, 255, 255), "Blue"),
        ((50, 100, 100), (70, 255, 255), "Green"),
        # Future enhancement: Support for yellow, orange, purple
        ((20, 100, 100), (40, 255, 255), "Yellow"),
        ((10, 100, 100), (20, 255, 255), "Orange"),
        ((130, 100, 100), (160, 255, 255), "Purple"),
    ]

    # Initialize webcam (0 for default webcam)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Detect colors and draw on frame
            result = detect_colors(frame, color_ranges)

            # Display result
            cv2.imshow("Color Detection", result)

            # Exit on 'q' key
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
