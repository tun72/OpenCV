import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv2.imread('imgs/lena.png', cv2.IMREAD_GRAYSCALE)

# Perform 2D FFT and shift the zero frequency to the center
fft_image = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft_image)

# Take log of the magnitude spectrum (for contrast enhancement)
magnitude_spectrum = np.abs(fft_shifted)
log_magnitude = np.log1p(magnitude_spectrum)

# Update the Fourier image with log-transformed magnitude
fft_shifted_log = fft_shifted / magnitude_spectrum * log_magnitude

# Inverse FFT to return to spatial domain
ifft_shifted_log = np.fft.ifftshift(fft_shifted_log)
image_log = np.fft.ifft2(ifft_shifted_log)
image_log = np.abs(image_log)

# Display original and log-transformed images
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Log-Transformed Image')
plt.imshow(image_log, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
