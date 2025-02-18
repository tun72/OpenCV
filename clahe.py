import cv2
import matplotlib.pyplot as plt

# file -> roll no

grayImg = cv2.imread("imgs/aheimage.png", 0)

equalize = cv2.equalizeHist(grayImg)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
adimg = clahe.apply(grayImg)

cv2.imshow("original", grayImg)
cv2.imshow("equalize", equalize)
cv2.imshow("clahe", adimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

