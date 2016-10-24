import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("lab", lab)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)