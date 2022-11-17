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


def hist_plot(img):

    count = []
    r = []

    for k in range(0, 256):
        r.append(k)
        count1 = 0

        for i in range(m):
            for j in range(n):
                if img[i, j] == k:
                    count1 += 1
        count.append(count1)

    return (r, count)


"""
Linear Contrast Stretch 
Max-Min Contrast Stretch Xnew=((Xınput-Xmin)/(Xmax-Xmin))*255
Histogram Equalization

s:çıktı pixeli
r: giriş pixeli
a ve b sırasıyla en küçük ve en büyük
c ve d sırasıyşa resimdeki en küçük ve en büyük pixel değerleri


Let a= maximum intensity level in the image
Let b= minimum intensity level in the image
Let rk= pixel value in the original image
Let sk= pixel value in the stretched image
constant= (255-0)/(a-b)

Then
sk= constant*rk

"""

"""
# To ascertain total numbers of rows and
# columns of the image, size of the image
m, n = img2.shape
r1, count1 = hist_plot(img2)

# plotting the histogram
plt.stem(r1, count1)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the original image')

# Transformation to obtain stretching
constant = (255 - 0) / (img2.max() - img2.min())
img_stretch = img2 * constant
r, count = hist_plot(img_stretch)

# plotting the histogram
plt.stem(r, count)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the stretched image')

# Storing stretched Image
cv2.imwrite('Stretched Image 2.png', img_stretch)

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

