import numpy as np
import pathlib
import cv2
from pathlib import Path
from matplotlib import pyplot as plt

path = str(Path(pathlib.Path().absolute()).parents[0])
path+="\\Pictures"
#Gri tonlarda bir resim yükle
img1 = cv2.imread(path+'\\picture1.jpg',cv2.IMREAD_COLOR) #1 //BGR
img2 = cv2.imread(path+'\\picture2.jpg',cv2.IMREAD_GRAYSCALE) #0
img3 = cv2.imread(path+'\\picture3.jpg',cv2.IMREAD_UNCHANGED) #-1

img4 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

R,G,B=cv2.split(img4)

output1_R=cv2.equalizeHist(R)
output1_G=cv2.equalizeHist(G)
output1_B=cv2.equalizeHist(B)

output1=cv2.merge((output1_R,output1_G,output1_B))
plt.hist(output1.flat, bins=100, range=(0,255))
plt.show()


clahe = cv2.createCLAHE(clipLimit=5) #Contrast Limited Adaptive Histogram Equazation
final_img = clahe.apply(img2) + 30

plt.hist(final_img.flat, bins=100, range=(0,255))
plt.show()

# Ordinary thresholding the same image
_, ordinary_img = cv2.threshold(img4, 155, 255, cv2.THRESH_BINARY)

# Showing all the three images
cv2.imshow("ordinary threshold", ordinary_img)
cv2.imshow("CLAHE image", final_img)


"""
Linear Contrast Stretch
Max-Min Contrast Stretch
Histogram Equalization

s:çıktı pixeli
r: giriş pixeli
a ve b sırasıyla en küçük ve en büyük
c ve d sırasıyşa resimdeki en küçük ve en büyük pixel değerleri
"""


size_y = img2.shape[0] # get shape
size_x = img2.shape[1]

flattened = img2.reshape([size_x*size_y])  # Flatten matrices

hist256,_ ,_ = plt.hist(flattened, bins=256)# ,log=True)
plt.show()

hist32,_ ,_ = plt.hist(flattened, bins=32)# ,log=True)
plt.show()

hist8,_ ,_ = plt.hist(flattened, bins=8)# ,log=True)
plt.show()

