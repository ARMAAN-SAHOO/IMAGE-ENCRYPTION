import cv2
import os

# Define the directory to save the captured images
save_directory = "images"

# Create the directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Initialize the webcam
cam = cv2.VideoCapture(0)  # Use 0 for the default webcam, change accordingly if using an external webcam

# Define the number of images to capture
num_images = 3

# Loop to capture multiple images
for i in range(num_images):
    # Capture frame-by-frame
    ret, frame = cam.read()

    # Display the captured frame
    cv2.imshow('Captured Image', frame)
    
    # Save the captured image
    image_name = os.path.join(save_directory, f"image_{i}.png")
    cv2.imwrite(image_name, frame)
    print(f"Image {i} captured and saved.")

    # Wait for a key press to capture the next image
    cv2.waitKey(1000)  # Adjust the delay time as needed

# Release the webcam and close OpenCV windows
cam.release()
cv2.destroyAllWindows()