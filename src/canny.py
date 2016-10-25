import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help="Path to image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"])

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5,5), 0)
# Gradients < 30 or > 150 will not be considered as edges. Gradients in btwn 30 and 150 will be classified based on how their intensities are connected
canny = cv2.Canny(img, 30, 150)
cv2.imshow("canny", canny)
cv2.waitKey(0)
