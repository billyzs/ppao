import numpy as np
import glob
import argparse
import cv2
def auto_canny(img, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(img)

    # apply automatic Canny edge detector using computed median
    lower = int(max(0, (1.0-sigma)*v))
    upper = int(min(255, (1.0+sigma)*v))
    return cv2.Canny(img, lower, upper)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help="Path to image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(img, (3,3), 0)

loose = cv2.Canny(blurred, 10, 200)
tight = cv2.Canny(blurred, 225, 250)
auto = auto_canny(blurred)
cv2.imshow("loose, tight, auto", np.hstack([loose, tight, auto]))
cv2.waitKey(0)
