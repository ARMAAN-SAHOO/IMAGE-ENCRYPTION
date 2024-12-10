import cv2
import numpy as np
import processimage as p
import EncryptionDecryption as ED

def calculate_entropy(image):
    entropy_list = []
    for channel in range(image.shape[2]):  # Iterate over each channel
        # Flatten the channel
        flat_channel = image[:,:,channel].flatten()

        # Calculate the histogram
        histogram, _ = np.histogram(flat_channel, bins=256, range=[0, 256])

        # Normalize histogram
        histogram_normalized = histogram / float(np.sum(histogram))

        # Calculate entropy
        entropy = -np.sum(histogram_normalized * np.log2(histogram_normalized + 1e-10))
        #Adding a small value like (1e-10) is a common practice to avoid taking the logarithm of zero. It has negligible effect on the overall entropy calculation.

        entropy_list.append(entropy)

    return entropy_list

# Load the original and encrypted images
image_path = 'input.png'
image_path = p.convert_to_png(image_path)
img = cv2.imread(image_path)

encrypted_img=ED.encryption(img)

# Calculate entropy for each channel
entropy_original = calculate_entropy(img)
entropy_encrypted = calculate_entropy(encrypted_img)

# Print the entropy of each channel for both images
print("Entropy of original image:")
print("Red channel:", entropy_original[0])
print("Green channel:", entropy_original[1])
print("Blue channel:", entropy_original[2])

print("\nEntropy of encrypted image:")
print("Red channel:", entropy_encrypted[0])
print("Green channel:", entropy_encrypted[1])
print("Blue channel:", entropy_encrypted[2])
