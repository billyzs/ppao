import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",required=True, help="Path to image")

args = vars(ap.parse_args())

img = cv2.imread(args["image"])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# compute the gradient magnitude image using Laplacian method
lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

# Sobel gradient representations

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.abs(sobelX))
sobelY = np.uint8(np.abs(sobelY))
sobelCombined = cv2.bitwise_or(sobelY, sobelX)
cv2.imshow("sobel x", sobelX)
cv2.imshow("sobel y", sobelY)
cv2.imshow("Sobel combined", sobelCombined)
cv2.waitKey(0)
