import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('imgs/lena.png')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv[:,:,2] = cv2.equalizeHist(hsv[:,:,2])

imageH = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# show image using plt
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(imageH)
plt.title('Enhance Image')
plt.show()


# show image using cv2
cv2.imshow('Original', image)
cv2.imshow('Enhance Image', imageH)
cv2.waitKey(0)
cv2.destroyAllWindows()

