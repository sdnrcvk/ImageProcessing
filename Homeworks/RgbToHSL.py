import pathlib
from pathlib import Path
import cv2

#RGB to HSL

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

# read the input RGB image as BGR format
bgr_img = cv2.imread(path+'\\picture3.jpg')
# Convert the BGR image to HSV Image
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

# Display the HSV image
cv2.imshow('BGR image', bgr_img)
cv2.imshow('HSV image', hsv_img)
cv2.waitKey(0)
cv2.destroyAllWindows()