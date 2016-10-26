import numpy as np
import argparse
import cv2
from auto_canny import auto_canny

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help="Path to image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(img, (3,3), 0)
# edged = cv2.Canny(blurred, 30, 150)
edged = auto_canny(blurred)
# cv2.imshow("edges", edged)
(_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("Counted {} contours in image".format(len(cnts)))

coins = cv2.imread(args["image"])
# cv2.drawContours(coins, cnts, -1, (0, 0, 255), 2)
# cv2.imshow("contours", coins)
for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv2.boundingRect(c)
    subimage = coins[y:y+h, x:x+w]
    cv2.imshow("coins", subimage)
    mask = np.zeros(subimage.shape[:2], dtype="uint8")
    ((cX, cY), r) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(cX-x), int(cY-y)), int(r), 255, -1)
    cv2.imshow("masked coin", cv2.bitwise_and(subimage, subimage, mask=mask))
    cv2.waitKey(0)


