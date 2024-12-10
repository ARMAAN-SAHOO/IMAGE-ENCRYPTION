# check number of unmatched pixels and equality
import cv2
import numpy as np
import processimage as p
import EncryptionDecryption as ED

def count_unmatching_pixels(image1, image2):
    diff_pixels = np.sum(image1 != image2)
    return diff_pixels

image_path = 'input.png'
image_path=p.convert_to_png(image_path)
image1 = cv2.imread(image_path)
encrypted_img=ED.encryption(image1)
image2=ED.decryption(encrypted_img)
cv2.imshow("original Image",image1)
cv2.imshow("Decrypted Image",image2)
cv2.waitKey(5000)
if np.array_equal(image1, image2):
    print("The images are identical.")
else:
    num_unmatching_pixels = count_unmatching_pixels(image1, image2)
    print("The images are not identical. Number of unmatching pixels:",num_unmatching_pixels)
    converted_image_array=cv2.bitwise_xor(image1,image2)
    cv2.imshow('Converted Image3', converted_image_array)
    cv2.waitKey(0)
#image3=image1-image2
#cv2.imshow('identical',image3)

