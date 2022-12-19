import cv2
import pathlib
from pathlib import Path
import numpy as np

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

# Görüntüyü oku
image = cv2.imread(path+'\\plaka.jpg')

# Görüntüyü gri tonlamaya dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntüyü kenar belirleme algoritması ile işle
edges = cv2.Canny(gray, 50, 150, apertureSize = 3)

#Açılma(Opening)
kernel = np.ones((5,5),dtype=np.uint8)

whiteNoise = np.random.randint(0,2,size=gray.shape[:2])
whiteNoise = whiteNoise*255
noise_img = whiteNoise + gray

opening = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)

#Kapanma(Closing)
blackNoise = np.random.randint(0,2,size=gray.shape[:2])
blackNoise = blackNoise*-255
noise_img = blackNoise + gray
noise_img[noise_img <=-245] = 0

closing = cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)

# Kenarları görüntüle
cv2.imshow('Orijinal',image)
cv2.imshow('Edges', edges)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

