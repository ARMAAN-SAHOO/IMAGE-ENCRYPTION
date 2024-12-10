import numpy as np
import PseudoRandomNumberGenerator as PRNG
import cv2
import math

def store(block_size):
    imgWidth = block_size[0]#image.shape[1]  # must be fixed as 512
    imgHeight = block_size[1]#image.shape[0]

    A = 2.5  # 2.3 to 3 for cubic map
    x0 = 0.1
    num_steps = imgWidth*imgHeight*3*8//8  # 512*512*3*8//8
    num_bits = 8
    print("Number of steps in cubic:",num_steps)
    cubicRNGtemp = PRNG.hem_cubic_map(A, x0, num_steps, num_bits)
    cubicRNG=[int(cubicRNGtemp[i],2) for i in range(len(cubicRNGtemp))]
    #print(cubicRNG)
    np.save("cubicRNG.npy",cubicRNG)

    A = 16  # 15 to 22.2 for rickers map
    x0 = 0.1
    v=math.ceil(math.log(max(imgWidth,imgHeight),2))
    num_steps = imgWidth*imgHeight*3*v//v  # 512*512*3*9//9
    num_bits = v
    print("Number of steps in rickers:",num_steps)
    rickersRNGtemp = PRNG.rickers_population_map(A, x0, num_steps, num_bits)
    rickersRNG=[int(rickersRNGtemp[i],2) for i in range(len(rickersRNGtemp))]
    #print(rickersRNG)
    np.save("rickersRNG.npy",rickersRNG)


