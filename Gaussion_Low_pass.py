import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imgs/lena.png', 0)

f = np.fft.fft2(img)
fShift = np.fft.fftshift(f)

M,N = img.shape
H = np.zeros((M,N), np.float32)
D0 = 10

# U ---> V

for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)

        H[u,v] = np.exp(-D**2 / (2*D0**2))



G = fShift * H

GShift = np.fft.ifft2(np.fft.ifftshift(G))

GShiftAbs = np.abs(GShift)

# freqShiftImg = np.asarray(GShift, np.uint8)

plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(img)

plt.subplot(1,2,2)
plt.title('Gaussion Blur')
plt.imshow(GShiftAbs)

plt.show()

# cv2.imshow("Original", img)
# cv2.imshow('G', GShiftAbs)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Load the image in grayscale
# img = cv2.imread('imgs/lena.png', 0)
#
# # Apply FFT
# f = np.fft.fft2(img)
# fShift = np.fft.fftshift(f)
#
# # Get image dimensions
# M, N = img.shape
#
# # Create the Gaussian filter
# H = np.zeros((M, N), np.float32)
# D0 = 10  # Cutoff frequency
#
# # Construct the filter
# for u in range(M):
#     for v in range(N):
#         D = np.sqrt((u - M / 2) ** 2 + (v - N / 2) ** 2)
#         H[u, v] = np.exp(-D**2 / (2 * D0**2))
#
# # Apply the filter in the frequency domain
# G = fShift * H
#
# # Apply the inverse FFT
# GShift = np.fft.ifft2(np.fft.ifftshift(G))
#
# freqShiftImg = np.asarray(GShift, np.uint8)

# Take the real part and normalize it to display
# GShift = np.real(GShift)
# GShift = np.clip(GShift, 0, 255).astype(np.uint8)

# Display the results
# cv2.imshow("Original", img)
# cv2.imshow('Filtered', freqShiftImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

