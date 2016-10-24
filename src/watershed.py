import numpy as np
import argparse
import cv2
from skimage.feature import peak_local_max
from skimage.morphology import watershed
from scipy import ndimage

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help="Path to image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"])

shifted = cv2.pyrMeanShiftFiltering(img, 21, 51)
peak_local_max
gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
(_, thresh) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# cv2.imshow("thresh", thresh)
# cv2.waitKey(0)
# compute the Euclidean distance from ever binary pixel to the nearest zero pizel, then find peaks in this distance map

thresh = cv2.medianBlur(thresh, 3)
D = ndimage.distance_transform_edt(thresh)

# find peaks (local max), ensure at leasr 20 pixels between peaks
localMax = peak_local_max(D, indices = False, min_distance = 20, labels=thresh)

# performs a connected component analysis on the local pieaks using 8-connectivity, then apply watershed algorithm
markers = ndimage.label(localMax, structure=np.ones((3,3)))[0]
labels = watershed(-D, markers, mask=thresh)  # guess: labels is of the same size as the input image, each entry is the peak that the pixel belongs to

print("{} unique segments found".format(len(np.unique(labels))-1))

# loop over labels
for label in np.unique(labels):
    if label == 0:
        continue
    mask = np.zeros(gray.shape, dtype='uint8')
    mask[labels == label] = 255
    # detect contours in the mask and grab the largest one
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)[-2]
    c = max(cnts, key=cv2.contourArea)
    ((x,y), r) = cv2.minEnclosingCircle(c)
    cv2.circle(img, (int(x), int(y)),int(r), (0,255,0), 2)
    cv2.putText(img, "#{}".format(label), (int(x)-10, int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255,), 2)

cv2.imshow("output", img)
cv2.waitKey(0)
