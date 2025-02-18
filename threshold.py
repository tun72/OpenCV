import cv2
import matplotlib.pyplot as plt
img = cv2.imread("imgs/lena.png")

ret,timg1 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO)
_,timg2 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO_INV)
_,timg3 =  cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
_,timg3 = cv2.threshold(img, 127,255,cv2.THRESH_BINARY_INV)
# _,timg4 = cv2.threshold(img, 127,255,cv2.THRESH_OTSU)


plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1,2,2)
plt.imshow(timg1)
plt.title('Thresholded Image')

plt.show()
#
#
# plt.waitforbuttonpress()


# cv2.imshow("img",timg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

