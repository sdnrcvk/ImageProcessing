import numpy as np
import pathlib
import cv2
from pathlib import Path

#Logaritma Dönüşümü

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

image = cv2.imread(path+'\\picture2.jpg')


c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))


log_image = np.array(log_image, dtype=np.uint8)

cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Log Donusumu', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()