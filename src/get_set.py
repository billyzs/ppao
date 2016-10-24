from __future__ import print_function
import cv2
import argparse

ag = argparse.ArgumentParser()
ag.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ag.parse_args())

img = cv2.imread(args["image"])
slice = img[0:100, 0:100]  # top 100*100 square of img
cv2.imshow("slice", slice)
img[0:100, 0:100] = (0,255,0)
cv2.imshow("updated", img)
cv2.waitKey(0)

