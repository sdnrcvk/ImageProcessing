import numpy as np
import pathlib
import cv2
from pathlib import Path

#Prewitt

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"
image = cv2.imread(path+'\\picture2.jpg',cv2.IMREAD_GRAYSCALE) #0

# remove noise
image_gaussian = cv2.GaussianBlur(image,(3,3),0)

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
image_prewittx = cv2.filter2D(image_gaussian, -1, kernelx)
image_prewitty = cv2.filter2D(image_gaussian, -1, kernely)
image_prewitt = image_prewittx + image_prewitty


cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Previtt x', image_prewittx)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Previtt y', image_prewitty)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Previtt', image_prewitt)
cv2.waitKey(0)
cv2.destroyAllWindows()
