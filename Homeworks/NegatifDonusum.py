import pathlib
import cv2
from pathlib import Path

#Negatif Dönüşüm

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

image = cv2.imread(path+'\\picture2.jpg') # Need to be sure to have a 8-bit input
image_gray = cv2.imread(path+'\\picture2.jpg',cv2.IMREAD_GRAYSCALE) # Need to be sure to have a 8-bit input

colored_negative = abs(255-image)
gray_negative = abs(255-image_gray)

cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Orijinal Gri', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Negatif', colored_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Negatif Gri', gray_negative)
cv2.waitKey(0)
cv2.destroyAllWindows()