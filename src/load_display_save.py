#!/bin/bash python

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
ap.add_argument("-m", "--method", required=False, help="how to show image. plt for matplotlib; defaults to cv2.imshow")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

method = args["method"]
if method == "plt":
    import matplotlib.pyplot as plt
    # import matplotlib.image as mpimg
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # plt expects RGB image but cv2 defaults to BGR
    plt.show()
else:
    cv2.imshow("image", image)
    cv2.imw
    cv2.waitKey(0)
