import cv2
import numpy as np
import argparse
from math import sqrt
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("original", img)

M = np.float32([[1, 0, 25], [0,1, 50]])
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

cv2.imshow("shifted down and right", shifted)
cv2.waitKey(0)
"""
a = sqrt(2) / 2
up_left = np.float32([[a, a, 0], [-a, a, 0]])
shifted = cv2.warpAffine(img, up_left, (img.shape[1], img.shape[0]))
cv2.imshow("shifted up and left", shifted)
cv2.waitKey(0)
"""
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
rot = cv2.getRotationMatrix2D(center, 45, 1)
print(rot)
rotated = cv2.warpAffine(img, rot, (w, h))
cv2.imshow("rotated", rotated)
cv2.waitKey(0)
