
import cv2
import numpy as np

import processimage as p
import EncryptionDecryption as ED
def calculate_npcr_uaci(img1, img2):

    # Initialize lists to store NPCR and UACI values for each channel
    npc_rate_channels = []
    uaci_channels = []

    # Iterate over each channel (assuming images are in BGR format)
    for channel in range(img1.shape[2]):
        diff_pixels = np.sum(img1[:,:,channel] != img2[:,:,channel])
        total_pixels = img1.shape[0]*img1.shape[1]
        print(diff_pixels,total_pixels)
        npc_rate = diff_pixels / total_pixels * 100
        npc_rate_channels.append(npc_rate)

        # Calculate UACI for the channel
        uaci = np.sum(np.abs(img1[:,:,channel].astype(np.int16) - img2[:,:,channel].astype(np.int16)))/(255*img1.shape[0]*img1.shape[1])*100
        uaci_channels.append(uaci)


    return npc_rate_channels,uaci_channels

# Load plaintext and ciphertext images
image_path = 'input.png'
image_path = p.convert_to_png(image_path)
plaintext_img1 = cv2.imread(image_path)
#plaintext_img2 = CP.change(image_path,1)

ciphertext_img1 = ED.encryption(plaintext_img1)
#ciphertext_img2 = ED.encryption(plaintext_img2)

# Calculate NPCR and UACI
npcr,uaci= calculate_npcr_uaci(plaintext_img1, ciphertext_img1)

# Print results for each channel
print("NPCR (Number of Pixel Change Rate):")
for channel, npc in enumerate(npcr):
    print(f"Channel {channel + 1}: {npc}%")

print("\nUACI (Unified Average Changed Intensity):")
for channel, uaci_val in enumerate(uaci):
    print(f"Channel {channel + 1}: {uaci_val}%")

