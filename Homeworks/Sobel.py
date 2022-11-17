import pathlib
import cv2
from pathlib import Path

#Sobel

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

image= cv2.imread(path+'\\picture2.jpg',cv2.IMREAD_GRAYSCALE)

# remove noise
image_gaussian = cv2.GaussianBlur(image,(3,3),0)

#sobel
image_sobelx = cv2.Sobel(image_gaussian,cv2.CV_8U,1,0,ksize=5)  # x
image_sobely = cv2.Sobel(image_gaussian,cv2.CV_8U,0,1,ksize=5)  # y
image_sobel = image_sobelx + image_sobely


cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Sobel x', image_sobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Sobel y', image_sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Sobel', image_sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()

