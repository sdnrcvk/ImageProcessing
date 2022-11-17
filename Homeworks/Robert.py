from scipy import ndimage
import numpy as np
import pathlib
import cv2
from pathlib import Path

#Robert

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

image_robert_x = np.array( [[1, 0 ],
						   [0,-1 ]] )

image_robert_y = np.array( [[ 0, 1 ],
						   [ -1, 0 ]] )

image = cv2.imread(path+'\\picture2.jpg',cv2.IMREAD_GRAYSCALE)

image_c = image.astype('float64')
image_c = image_c / 255 # rescale

image_c/=255.0

vertical = ndimage.convolve( image_c, image_robert_x )
horizontal = ndimage.convolve( image_c, image_robert_y )

image_robert = np.sqrt( np.square(horizontal) + np.square(vertical))
image_robert*=255

cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Robert', image_robert)
cv2.waitKey(0)
cv2.destroyAllWindows()