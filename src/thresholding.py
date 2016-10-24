import numpy as np
import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help="Path to image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("original", img)

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
# cv2.imshow("threshold binary", thresh)

(T, thresh_inv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("threshold inverted", thresh_inv)

# cv2.imshow("coins", cv2.bitwise_and(img, thresh_inv))
# cv2.waitKey(0)

# adaptive thresholding:

thresh = cv2.adaptiveThreshold(blurred, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("mean thresh", thresh)

g_thresh = cv2.adaptiveThreshold(blurred, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian thresh", g_thresh)
cv2.waitKey(0)


