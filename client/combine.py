import cv2
import numpy as np
import SplitAndProcess as SAP
import processimage as P
from datetime import *
def combine_blocks_to_image(processed_blocks, original_dims):
    # Create an empty array for the combined image
    combined_image = np.zeros((original_dims[0], original_dims[1], original_dims[2]), dtype=np.uint8)
    
    block_height, block_width = processed_blocks[0][0].shape[:2]
    
    for y, row_blocks in enumerate(processed_blocks):
        for x, block in enumerate(row_blocks):
            start_x = x * block_width
            start_y = y * block_height
            combined_image[start_y:start_y+block_height, start_x:start_x+block_width] = block
    
    return combined_image

def to_process(image_paths):
    image_path_encrypted=[]
    for image_path in image_paths:
        image_path=P.convert_to_png(image_path)
        block_size = (128,128)# Define the block size
        E_start=datetime.now()
        processed_blocksE,original_dims = SAP.split_and_process_image(image_path, block_size)
        combined_imageE = combine_blocks_to_image(processed_blocksE, original_dims)
        E_end=datetime.now()
        image_pathE=image_path[:-4]+"CombinedEncrypted"+image_path[-4:]
        image_path_encrypted.append(image_pathE)
        cv2.imwrite(image_pathE,combined_imageE)
        #cv2.imshow("Combined ImageEncrypted", combined_imageE)
        #cv2.waitKey(0)
        print("Encryption time:",E_end-E_start)
    return image_path_encrypted


# Alternatively, save the image using cv2.imwrite('path_to_save.jpg', combined_image)
