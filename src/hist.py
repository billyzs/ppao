import numpy as np
from matplotlib import pyplot as plt
import argparse
import cv2

def plot_histogram(img, title, mask=None):
    chans = cv2.split(img)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask=mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
gray_img = np.ones((300, 300), dtype="uint8") * 128
gray_img[0:150, :] = 0

# pyplot histogram
plt.hist(gray_img.ravel(), 256, [0,256])
plt.title('Histogram for gray scale picture')
# plt.show()

# cv histogram
numBins = 256
hist = cv2.calcHist([gray_img], [0], None, [numBins], [0, 256])
plt.figure()
plt.plot(hist)
plt.xlim([0, numBins])
# plt.show()

# histogram for colored image
chans = cv2.split(img)
colors = ['b', 'g', 'r']
plt.figure()
plt.title("flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# pixels")

hist = cv2.calcHist([img], [0], None, [numBins], [0,256])
plt.plot(hist)
# plt.show()

for (channel, color) in zip(chans, colors):
    hist = cv2.calcHist([channel], [0], None, [numBins], [0, 256])
    plt.xlim([0, numBins])
    plt.plot(hist, color=color)
# plt.show()

# 2D histogram
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color histogram for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color histogram for B and R")
plt.colorbar(p)

# plt.show()





