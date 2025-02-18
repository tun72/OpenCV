import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = cv2.imread('imgs/logo_GS.png', 1)

# RECOLOR the image
# b,g,r = cv2.split(img)
# img[:,:,0] = 255
# for i in range(100):
#     for j in range(100):
#         img[i,j] = [255,234,100]

# RESIZE IMAGE
#img.shape[:2]
h,w,ch = img.shape
# resize_img = cv2.resize(img,(int(w/4), int(h/4)), interpolation = cv2.INTERSECT_FULL)


matrix = cv2.getRotationMatrix2D((int(w/2), int(h/2)), 270, 1)
rotate = cv2.warpAffine(img, matrix, (w,h))

cv2.imshow('resize_image', rotate)




# IMAGE AWAIT AND CLOSE
# image write
key = cv2.waitKey(0)
# if key==ord("s"):
#     cv2.imwrite("logo_GS.png", resize_img)
cv2.destroyAllWindows()