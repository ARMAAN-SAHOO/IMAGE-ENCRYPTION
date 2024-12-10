import cv2
import numpy as np
import LoadCubicRicker as LCR
import Decryption as ED
def process_blockD(block):
    #rblock=ED.encryption_decryption(block,x,y)
    Dblock=ED.decryption(block)
    return Dblock

def split_and_process_image(image_path, block_size):
    # Read the image
    
    image = cv2.imread(image_path)
    
    # Get image dimensions
    height, width, channels = image.shape
    print("Image shape:",image.shape)

    #Load Cubic and Ricker
    LCR.store(block_size)
    # Calculate the number of blocks in both dimensions
    num_blocks_vertical = height // block_size[1]
    num_blocks_horizontal = width // block_size[0]
    
    # List to store processed blocks
    processed_blocks=[]
    # Process each block
    z=0
    for y in range(0, num_blocks_vertical):
        row_blocks=[]
        for x in range(0, num_blocks_horizontal):
            # Compute the coordinates of the current block
            start_x = x * block_size[0]
            start_y = y * block_size[1]
            end_x = start_x + block_size[0]
            end_y = start_y + block_size[1]
            
            # Extract the block from the image
            block = image[start_y:end_y, start_x:end_x]

            #cv2.imshow('block'+str(z),block)
            z+=1
            #  Process the block
            
            processed_block = process_blockD(block)
            row_blocks.append(processed_block)
        processed_blocks.append(row_blocks)
    #cv2.waitKey(0)
    print("Number of blocks during decryption:",z)
    return processed_blocks,(height, width, channels)
