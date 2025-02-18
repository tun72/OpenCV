import cv2
import matplotlib.pyplot as plt

# file -> roll no

grayImg = cv2.imread("imgs/professor.png", 0)
# histo_img = cv2.calcHist([grayImg], [1], None, [256], [0, 256])
# plt.imshow(histo_img)
# plt.show()

equalize = cv2.equalizeHist(grayImg)

cv2.imshow("professor_original", grayImg)
cv2.imshow("equalize", equalize)

cv2.waitKey(0)
cv2.destroyAllWindows()

