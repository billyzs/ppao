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
cv2.waitKey(0)
(h, w) = img.shape[:2]

new_h = 300
new_w = new_h * w // h

resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
cv2.imshow("resized to {} by {}".format(new_w, new_h), resized)
cv2.waitKey(0)