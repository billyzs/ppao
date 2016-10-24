import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
(B, G, R) = cv2.split(img)
zeros = np.zeros(img.shape[:2], dtype='uint8')
splitted = [B, G, R]
for i in range(0, len(splitted)):
    merged_img = [zeros, zeros, zeros]
    merged_img[i] = splitted[i]
    cv2.imshow("merged", cv2.merge(merged_img))
    cv2.waitKey(0)
cv2.destroyAllWindows()
