# reversible rickers Horizontal
import cv2
import numpy as np
import processimage as p
def cubic(source,imgWidth,imgHeight,cubicRNG):
    for i in range(imgHeight):
        for j in range(imgWidth):
            for k in range(3):  # for each channel (RGB)
                source[i][j][k] = source[i][j][k]^cubicRNG[(imgWidth * i + j + k * imgWidth * imgHeight)]
def rickersHorizontalUnique(imgWidth,imgHeight,rickersRNG):
    d={}
    for i in range(imgHeight):
        for j in range(imgWidth):
            for k in range(3):
                x1=rickersRNG[imgWidth*i+j+k*imgWidth*imgHeight]
                x1=x1%imgWidth
                d[x1]=(i,j,k)
    D={d[x]:x for x in d}
    #remove transitivity
    D2={}
    t=list(D.keys()) # keys
    for i in D:
        if (i[0],D[i],i[2]) not in t:
            D2[i]=D[i]
    return D2
def rickersVerticalUnique(imgWidth,imgHeight,rickersRNG):
    d={}
    for i in range(imgWidth):
        for j in range(imgHeight):
            for k in range(3):
                x1=rickersRNG[imgHeight*i+j+k*imgWidth*imgHeight]
                x1=x1%imgHeight
                d[x1]=(j,i,k)
    D={d[x]:x for x in d}
    D2={}
    t=list(D.keys())
    for i in D:
        if (D[i],i[1],i[2]) not in t:
            D2[i]=D[i]
    return D2  
def rickersHorizontal(source,D,imgWidth,imgHeight):
    for i in range(imgHeight):
        for j in range(imgWidth):
            for k in range(3):
                if (i,j,k) in D:
                    x1=D[(i,j,k)]
                    temporary=source[i,j,k]
                    source[i,j,k]=source[i,x1,k]
                    source[i,x1,k]=temporary
                     
def rickersVertical(source,D,imgWidth,imgHeight):
    for i in range(imgHeight):
        for j in range(imgWidth):
            for k in range(3):
                if (i,j,k) in D:
                    x1=D[(i,j,k)]
                    temporary=source[i,j,k]
                    source[i,j,k]=source[x1,j,k]
                    source[x1,j,k]=temporary
def decryption(block):
    image=block

    # Define image width and height
    imgWidth = image.shape[1]
    imgHeight = image.shape[0]
    
    # Load the stored 3D array
    cubicRNG = np.load("cubicRNG.npy")
    rickersRNG = np.load("rickersRNG.npy")

    decryptedRickersVertical = np.zeros_like(image)
    decryptedRickersHorizontal = np.zeros_like(image)
    decryptedCubic = np.zeros_like(image)

    # Perform encryption and decryption
   

    D_Horizontal=rickersHorizontalUnique(imgWidth,imgHeight,rickersRNG)
    D_Vertical=rickersVerticalUnique(imgWidth,imgHeight,rickersRNG)

    np.copyto(decryptedRickersVertical,image)
    rickersVertical(decryptedRickersVertical,D_Vertical,imgWidth,imgHeight)

    np.copyto(decryptedRickersHorizontal,decryptedRickersVertical)
    rickersHorizontal(decryptedRickersHorizontal,D_Horizontal,imgWidth,imgHeight)

    np.copyto(decryptedCubic,decryptedRickersHorizontal)
    cubic(decryptedCubic,imgWidth,imgHeight,cubicRNG)
    
    return decryptedCubic
