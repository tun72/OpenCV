import cv2
import matplotlib.pyplot as plt
import numpy as np

# file -> roll no
# basic kernel
img = cv2.imread("imgs/professor.png", 1)

# kernel = np.ones((3,3),np.uint8)/9  # divided by 9 to calc average

# Identity matrix
kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]], np.float32)

# edges detection kernel
kernel1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]], np.float32)

# sharpen kernel
kernel2 = np.array([[0, -1, 0], [-1, 6, -1], [0, -1, 0]], np.float32)

# blur
kernel3 = np.ones((5,5), np.float32)/25



filterImg = cv2.filter2D(img, -1, kernel)
filterImg1 = cv2.filter2D(img, -1, kernel1)
filterImg2 = cv2.filter2D(img, -1, kernel2)
filterImg3 = cv2.filter2D(img, -1, kernel3)

# cv2.imshow("original", img)
# cv2.imshow("filter", filterImg)

plt.subplot(2,3,1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(2,3,2)
plt.imshow(filterImg)
plt.title('Identity Image')

plt.subplot(2,3,3)
plt.imshow(filterImg1)
plt.title('Edges Detection')

plt.subplot(2,3,4)
plt.imshow(filterImg2)
plt.title('Sharpen Image')

plt.subplot(2,3,5)
plt.imshow(filterImg3)
plt.title('Blur Image')

plt.show()



