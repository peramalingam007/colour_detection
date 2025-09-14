import cv2
import numpy as np
import os

def detect_colors(image_path, output_dir="output"):
    """
    Detects yellow, orange, and purple colors in an image using HSV ranges.
    Saves the detected color regions as separate images.
    
    Args:
        image_path (str): Path to the input image.
        output_dir (str): Directory to save output images.
    """
    try:
        # Check if the image file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file '{image_path}' not found.")

        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Failed to load image '{image_path}'. Check file format or path.")

        # Convert to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Define HSV ranges for yellow, orange, and purple
        colors = {
            'yellow': ([20, 100, 100], [30, 255, 255]),
            'orange': ([8, 100, 100], [20, 255, 255]),
            'purple': ([130, 100, 100], [160, 255, 255])
        }

        # Process each color
        for color_name, (lower, upper) in colors.items():
            try:
                # Convert HSV ranges to numpy arrays
                lower_bound = np.array(lower, dtype=np.uint8)
                upper_bound = np.array(upper, dtype=np.uint8)

                # Create mask for the color
                mask = cv2.inRange(hsv, lower_bound, upper_bound)

                # Optional: Apply morphological operations to reduce noise
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

                # Apply mask to original image
                result = cv2.bitwise_and(image, image, mask=mask)

                # Save the result
                output_path = os.path.join(output_dir, f"{color_name}_detected.jpg")
                cv2.imwrite(output_path, result)
                print(f"Saved {color_name} detection to {output_path}")

                # Optional: Display the result (comment out if not needed)
                # cv2.imshow(f"{color_name} detection", result)

            except Exception as e:
                print(f"Error processing color {color_name}: {str(e)}")

        # Optional: Display original image (comment out if not needed)
        # cv2.imshow("Original Image", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    except Exception as e:
        print(f"Error in detect_colors: {str(e)}")

def main():
    # Example usage
    image_path = "image.jpg"  # Replace with your image path
    output_dir = "color_detection_output"  # Output directory

    try:
        detect_colors(image_path, output_dir)
        print("Color detection completed successfully.")
    except Exception as e:
        print(f"Error in main: {str(e)}")

if __name__ == "__main__":
    main()
