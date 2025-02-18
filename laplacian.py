import cv2
import numpy as np

img = cv2.imread('./imgs/lena.png')

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    canny = cv2.Canny(frame, 100, 150)
    sobel = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    Laplacian=cv2.Laplacian(frame, cv2.CV_64F)


    cv2.imshow('Canny', canny)
    cv2.imshow('Laplacian', Laplacian)
    cv2.imshow('Sobel', sobel)
    waitkey=cv2.waitKey(5)

    if(waitkey==ord('q')):
        
        break

cam.release()
cv2.destroyAllWindows()

# cany = cv2.Laplacian(img, cv2.CV_64F)
# sobal = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3) #odd number 3,5, 7,9...
#
#

# cv2.imshow('Edge', sobal)



