import cv2
import numpy as np

def detect_colors(frame, color_ranges, debug=False, combined_mask=None):
    """
    Detects colors in the frame based on HSV ranges and draws bounding boxes.
    
    Args:
        frame: Input BGR image from webcam.
        color_ranges: List of tuples [(lower_hsv, upper_hsv, color_name), ...].
        debug: If True, visualizes individual HSV masks.
        combined_mask: Optional output for combined mask (for debug visualization).
    
    Returns:
        Frame with bounding boxes drawn around detected colors.
    """
    # Convert frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Initialize output frame
    result = frame.copy()
    
    # Initialize combined mask for debug
    if debug:
        combined_mask = np.zeros_like(hsv[:,:,0])  # Grayscale mask
    
    for idx, (lower, upper, color_name) in enumerate(color_ranges):
        # Create mask for the color range
        lower = np.array(lower)
        upper = np.array(upper)
        mask = cv2.inRange(hsv, lower, upper)
        
        # Optional: Apply morphological operations to reduce noise
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        # If debug, show individual mask
        if debug:
            cv2.imshow(f"Mask - {color_name}", mask)
            combined_mask = cv2.bitwise_or(combined_mask, mask)
        
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw bounding boxes for detected regions
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Ignore small contours (noise)
                x, y, w, h = cv2.boundingRect(contour)
                # Draw rectangle and label
                cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.putText(result, color_name, (x, y - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
    
    if debug and combined_mask is not None:
        # Show combined mask in color for better visualization
        combined_mask_colored = cv2.cvtColor(combined_mask, cv2.COLOR_GRAY2BGR)
        cv2.imshow("Combined HSV Mask", combined_mask_colored)
    
    return result

def main():
    # Define HSV ranges for colors (including enhancements)
    color_ranges = [
        ((0, 100, 100), (10, 255, 255), "Red"),
        ((110, 100, 100), (130, 255, 255), "Blue"),
        ((50, 100, 100), (70, 255, 255), "Green"),
        ((20, 100, 100), (40, 255, 255), "Yellow"),
        ((10, 100, 100), (20, 255, 255), "Orange"),
        ((130, 100, 100), (160, 255, 255), "Purple"),
    ]

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Debug toggle
    debug = False

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            # Detect colors and draw on frame
            result = detect_colors(frame, color_ranges, debug=debug)

            # Display result
            cv2.imshow("Color Detection", result)

            # Key presses for controls
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('d'):
                debug = not debug
                print(f"Debug mode: {'ON' if debug else 'OFF'}")
                if not debug:
                    # Close debug windows when toggled off
                    for color_name in [c[2] for c in color_ranges]:
                        cv2.destroyWindow(f"Mask - {color_name}")
                    cv2.destroyWindow("Combined HSV Mask")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
