import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

gray_img = cv2.imread(args["image"])
gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
eq = cv2.equalizeHist(gray_img)

cv2.imshow("histogram equalization", np.hstack([gray_img, eq]))
cv2.waitKey(0)
