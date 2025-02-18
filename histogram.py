import cv2
import matplotlib.pyplot as plt
img = cv2.imread('imgs/lena.png')

histo_img = cv2.calcHist([img], [1], None, [256], [0, 256])
cv2.imshow("Original", img)
# cv2.imshow('histogram', histo_img)

# plt.hist(histo_img.ravel())
cv2.imshow("Histogram", histo_img)
plt.imshow(histo_img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()