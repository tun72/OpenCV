import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imgs/lena.png')

ksize = (10,10)

blurImg = cv2.blur(img,ksize)
gaussianBlur = cv2.GaussianBlur(img, (7, 7), 0)

medianBlur = cv2.medianBlur(img, 5)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)

cv2.imshow('Original Image',img)
cv2.imshow('Blurred Image',blurImg)
cv2.imshow('Gaussian Blurred Image',gaussianBlur)
cv2.imshow('Median Blurred Image',medianBlur)
cv2.imshow('Bilateral Filter',bilateralFilter)


cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(3,3,1)
# plt.imshow(img)
# plt.title('Original Image')
#
# plt.subplot(3,3,2)
# plt.imshow(blurImg)
# plt.title('Blurred Image')
#
# plt.subplot(3,3,3)
# plt.imshow(gaussianBlur)
# plt.title('Gaussian Blurred Image')
#
# plt.subplot(3,3,4)
# plt.imshow(bilateralFilter)
# plt.title('Bilateral Filter')
#
# plt.subplot(3,3,5)
# plt.imshow(medianBlur)
# plt.title('Median Blurred Image')
#
# plt.subplot(3,3,6)
# plt.imshow(bilateralFilter)
# plt.title('Bilateral Filter')
#
# plt.show()