import cv2
import numpy as np
import SplitAndProcess as SAP
import processimage as P
from datetime import *
def a(no_of_images):
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


    #image_paths = ["ReceivedImage1.png"]
    for i in range(no_of_images):
        file_path="ReceivedImage"+str(i+1)+".png"
        image_path=P.convert_to_png(file_path)
        block_size = (128,128)# Define the block size


        D_start=datetime.now()
        processed_blocksD,original_dims = SAP.split_and_process_image(image_path, block_size)
        combined_imageD = combine_blocks_to_image(processed_blocksD, original_dims)
        D_end=datetime.now()
        print("Decryption time:",D_end-D_start)
        image_pathD=image_path[:-4]+"CombinedDecrypted"+image_path[-4:]
        cv2.imwrite(image_pathD,combined_imageD)
        #cv2.imshow("Combined ImageDecrypted", combined_imageD)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # Alternatively, save the image using cv2.imwrite('path_to_save.jpg', combined_image)
