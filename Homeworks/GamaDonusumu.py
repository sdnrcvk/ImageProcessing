import numpy as np
import pathlib
import cv2
from pathlib import Path

#Gama Dönüşümü

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

image = cv2.imread(path+'\\picture2.jpg')

cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

for gamma in [3.0, 4.0, 5.0]:
    gamma_image = np.array(255 * (image / 255) ** gamma, dtype='uint8')
    cv2.imshow('Gama Donusumu', gamma_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

