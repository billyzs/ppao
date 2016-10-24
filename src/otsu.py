import numpy as np
import argparse
import cv2
import mahotas
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help="Path to image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (5,5), 0)
T = mahotas.thresholding.otsu(blurred)
print("T = {}".format(T))
thresh = img.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("otsu", np.hstack([img, thresh]))
cv2.waitKey(0)

# Riddler's thresholding:

T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: T = {}".format(T))
(_, thresh_rc) = cv2.threshold(img, T, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Riddler-Calvard", np.hstack([img, thresh_rc]))
cv2.waitKey(0)
