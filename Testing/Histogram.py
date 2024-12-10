# import required libraries
import cv2
from matplotlib import pyplot as plt
import numpy as np
import processimage as p
import EncryptionDecryption as ED
image_path = 'input.png'
image_path = p.convert_to_png(image_path)
img = cv2.imread(image_path)
encrypted_img=ED.encryption(img)

# define a function to compute and plot histogram
def plot_histogram(img, title):
    plt.title(title)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.hist(img.ravel(), 256, [0, 256])

# loop over the channels
for i, col in enumerate(['blue', 'green', 'red']):
    # split the image into channels
    channel = cv2.split(img)[i]
    encrypted_channel = cv2.split(encrypted_img)[i]
    
    # plot histogram for original image channel
    plt.figure(i + 1)
    plot_histogram(channel, f"Histogram for {col.capitalize()} Channel - Original Image")
    plt.xlim([0, 256])  # x-axis range from 0 to 256
    plt.ylim([0, 15000])  # y-axis range from 0 to 15000
    plt.xticks(np.arange(0, 257, step=50))  # x-axis ticks from 0 to 256 with each 50
    plt.yticks(np.arange(0, 15001, step=5000))  # y-axis ticks from 0 to 15000 with each 5000

    # plot histogram for encrypted image channel
    plt.figure(i + 4)
    plot_histogram(encrypted_channel, f"Histogram for {col.capitalize()} Channel - Encrypted Image")
    plt.xlim([0, 256])  # x-axis range from 0 to 256
    plt.ylim([0, 15000])  # y-axis range from 0 to 15000
    plt.xticks(np.arange(0, 257, step=50))  # x-axis ticks from 0 to 256 with each 50
    plt.yticks(np.arange(0, 15001, step=5000))  # y-axis ticks from 0 to 15000 with each 5000

# show the plots
plt.show()

'''# import required libraries
import cv2
from matplotlib import pyplot as plt
import numpy as np
import processimage as p

image_path = 'C:/Users/S AAKASH/Desktop/Miniproject/ImageProcessing/InDevelopment/Rectangular.jpg'
image_path = p.convert_to_png(image_path)
img = cv2.imread(image_path)

# define a function to compute and plot histogram
def plot_histogram(img, title):
   # split the image into blue, green and red channels
   channels = cv2.split(img)
   colors = ("b", "g", "r")
   plt.title(title)
   plt.xlabel("Bins")
   plt.ylabel("# of Pixels")
   # loop over the image channels
   for (channel, color) in zip(channels, colors):
      # compute the histogram for the current channel and plot it
      hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
      plt.plot(hist, color=color)
      plt.xlim([0, 256])

# compute a histogram for the image
plot_histogram(img, "Histogram for Image")

# show the plot
plt.show()
'''

