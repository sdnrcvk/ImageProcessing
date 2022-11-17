import numpy as np
import pathlib
import cv2
from pathlib import Path

#8 bitliğe dönüştürme

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

image = cv2.imread(path+'\\picture2.jpg',cv2.IMREAD_GRAYSCALE) # Need to be sure to have a 8-bit input

# Get input size
height, width = image.shape[:2]

# Desired "pixelated" size
w, h = (256, 256)

# Resize input to "pixelated" size
temp = cv2.resize(image, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
image8 = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
image16 = np.uint16(image8)*256


cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('8 Bit', image8)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('16 Bit', image16)
cv2.waitKey(0)
cv2.destroyAllWindows()

