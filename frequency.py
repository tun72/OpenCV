import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imgs/lena.png')

f = np.fft.fft2(img)
fShift = np.fft.fftshift(f)


# for color
fImg = 20*np.log1p(np.abs(f))
freqImg = np.asarray(fImg, np.uint8)

# frequency shift
fShiftImg = 20*np.log1p(np.abs(fShift))
freqShiftImg = np.asarray(fShiftImg, np.uint8)


plt.subplot(131)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(132)
plt.imshow(freqImg)
plt.title('Frequency Image')

plt.subplot(133)
plt.imshow(freqShiftImg)
plt.title('Frequency Shift Image')

plt.show()