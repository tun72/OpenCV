import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('imgs/lena.png')

ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
ycrcb[:,:,2] = cv2.equalizeHist(ycrcb[:,:,0])

imageY = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)

# show image using plt
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(imageY)
plt.title('Enhance Image')
plt.show()


# show image using cv2
cv2.imshow('Original', image)
cv2.imshow('Enhance Image', imageY)
cv2.waitKey(0)
cv2.destroyAllWindows()

