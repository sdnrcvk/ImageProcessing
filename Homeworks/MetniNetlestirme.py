import pathlib
import cv2
from pathlib import Path
import numpy as np

#Metni Netlestirme

print(cv2.__version__)

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"

image = cv2.imread(path+'\\picture7.png', cv2.IMREAD_GRAYSCALE)

image = image.astype(np.float32)
image = image / 255 # rescale
image = 1 - image # inversion. ink is the signal, white paper isn't

kernell = np.ones((5,5))

# estimates intensity of text
dilated = cv2.dilate(image, kernel=kernell)

# tweak this threshold to catch faint text but not background
textmask = (dilated >= 0.15)
# 0.05 catches background noise of 0.02
# 0.25 loses some text

# rescale text pixel intensities
# this will obviously magnify noise around faint text
enhanced = image / dilated

# copy unmodified background back in
# (division magnified noise on background)
enhanced[~textmask] = image[~textmask]

# invert again for output
output = 1 - enhanced

cv2.imshow('Orijinal', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Netlesmis', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
