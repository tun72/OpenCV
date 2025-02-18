import cv2
import numpy as np

img = cv2.imread('imgs/sf2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)


#  picture  max value * 0.01
# harris = cv2.cornerHarris(gray,2,3,0.04)
# img[harris > 0.01 * harris.max()] = [255, 255, 0]
# cv2.imshow('Harris Corner Point', img)

sift = cv2.SIFT_create()
# keypoints = sift.detect(gray, None)
# img = cv2.drawKeypoints(img, keypoints, None, color=(0, 0, 255))
# cv2.imshow('SIFT', img)

# describe
# key, des = sift.detectAndCompute(gray, None)
# key_color, des_color = sift.detectAndCompute(img, None)





# fast Corner
# fastCorner = cv2.FastFeatureDetector_create()
# keypoints = fastCorner.detect(gray, None)
#
# img = cv2.drawKeypoints(img, keypoints, None, color=(10, 100, 100))
#
# cv2.imwrite('imgs/fast_keypoints.jpg', img)
# cv2.imshow('img', img)


orb = cv2.ORB_create()
# detector
# kep, des = orb.detectAndCompute(gray, None)

# describer   # 1. ORB #2. SIFT two describer
kp, des = orb.detectAndCompute(gray, None)

img = cv2.drawKeypoints(img, kp, None, color=(100, 100, 100))

cv2.imshow('img', img)





cv2.waitKey(0)
cv2.destroyAllWindows()


