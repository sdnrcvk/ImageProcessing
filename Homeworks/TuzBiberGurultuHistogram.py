import random
import numpy as np
import pathlib
import cv2
from pathlib import Path
from matplotlib import pyplot as plt

#Tuz-Biber Gürültüsü Ekleme-Histogram

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

def add_noise(image):
    # Getting the dimensions of the image
    row, col = image.shape

    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to white
        image[y_coord][x_coord] = 255

    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord = random.randint(0, row - 1)

        # Pick a random x coordinate
        x_coord = random.randint(0, col - 1)

        # Color that pixel to black
        image[y_coord][x_coord] = 0

    return image

image = cv2.imread(path+'\\picture2.jpg',cv2.IMREAD_GRAYSCALE) #0
cv2.imshow('Orijinal',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hist,bins = np.histogram(image.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(image.flatten(),256,[0,256], color = 'b')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

salt_and_pepper_image=add_noise(image)
cv2.imshow('Salt and Pepper',salt_and_pepper_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hist,bins = np.histogram(salt_and_pepper_image.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(salt_and_pepper_image.flatten(),256,[0,256], color = 'b')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


