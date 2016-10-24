import cv2
import numpy as np
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage
import argparse
img = cv2.imread("../data/watershed_coins_01.jpg")
shifted = cv2.pyrMeanShiftFiltering(img, 21, 51)
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
(_, thresh) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# find contours in the thresholded image
countours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
print("{} unique contours found".format(len(countours)))
# OUT: 22 unique contours found
for (i, c) in enumerate(countours):
    # draw countours
    color = (0, 255 - 50 * i, 0)
    ((x,y), _) = cv2.minEnclosingCircle(c)
    cv2.putText(img, "#{}".format(i+1), (int(x)-10, int(y)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
    cv2.drawContours(img, [c], -1, color, 2)
cv2.imshow("contours", img)
cv2.waitKey(0)
