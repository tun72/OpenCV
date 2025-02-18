import cv2
import numpy as np


img1 = cv2.imread('imgs/lena.png')
img2 = cv2.rotate(img1, cv2.ROTATE_180)


# ORB ALGORITHM

# orb = cv2.ORB_create()
#
# kp1, des1 = orb.detectAndCompute(img1,None)
# kp2, des2 = orb.detectAndCompute(img2,None)
#
# # matching algo BrueForce
#
# matcher = cv2.BFMatcher()
# matches = matcher.match(des1,des2)
#
#
# compimg = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)
#
#
# cv2.imwrite('imgs/matches.jpg', compimg)
# cv2.imshow('img1', compimg)
# cv2.imshow('img2', img2)

# SIFT
sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

matcher = cv2.BFMatcher()
matches = matcher.match(des1,des2)

compimg = cv2.drawMatches(img1, kp1, img2, kp2, matches, None)

cv2.imwrite('imgs/matches_sift.jpg', compimg)
cv2.imshow('img1', compimg)

cv2.waitKey(0)
cv2.destroyAllWindows()