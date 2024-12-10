import cv2
import numpy as np
import processimage as p
import EncryptionDecryption as ED

def correlation_coefficients(image1, image2):
    correlations = {}
    # Compute correlation coefficients for each channel
    for i, color in enumerate(['blue', 'green', 'red']):
        channel_image1 = image1[:, :, i]
        channel_image2 = image2[:, :, i]

        # Compute mean intensities
        mean_channel_image1 = np.mean(channel_image1)
        mean_channel_image2 = np.mean(channel_image2)

        # Compute correlation coefficients
        horizontal_correlation = np.sum((channel_image1[:, :-1] - mean_channel_image1) * (channel_image2[:, 1:] - mean_channel_image2)) \
                                 / np.sqrt(np.sum((channel_image1[:, :-1] - mean_channel_image1) ** 2) * np.sum((channel_image2[:, 1:] - mean_channel_image2) ** 2))

        vertical_correlation = np.sum((channel_image1[:-1, :] - mean_channel_image1) * (channel_image2[1:, :] - mean_channel_image2)) \
                               / np.sqrt(np.sum((channel_image1[:-1, :] - mean_channel_image1) ** 2) * np.sum((channel_image2[1:, :] - mean_channel_image2) ** 2))

        correlations[color] = {'horizontal': horizontal_correlation, 'vertical': vertical_correlation}

    return correlations

# Load original and encrypted frames
image_path = 'input.png'
image_path = p.convert_to_png(image_path)
img = cv2.imread(image_path)
encrypted_img=ED.encryption(img)

# Compute correlation coefficients
coefficientsOriginal=correlation_coefficients(img,img)
coefficientsEncrypted = correlation_coefficients(encrypted_img, encrypted_img)

# Print correlation coefficients for each channel
for color in coefficientsOriginal:
    print(f"Color Channel: {color.capitalize()}")
    print("Horizontal Correlation Coefficient for original image:", coefficientsOriginal[color]['horizontal'])
    print("Horizontal Correlation Coefficient for encrypted image:", coefficientsEncrypted[color]['horizontal'])
    print()

for color in coefficientsOriginal:
    print(f"Color Channel: {color.capitalize()}")
    print("Vertical Correlation Coefficient for original image:", coefficientsOriginal[color]['vertical'])
    print("Vertical Correlation Coefficient for encrypted image:", coefficientsEncrypted[color]['vertical'])
    print()


