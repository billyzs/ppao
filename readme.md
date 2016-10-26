# Notes
## Notations and conventions
### Coordinate system
OpenCV uses a coordinate system defined as follows:

* The origin of the coordinate system is on the top left corner of the image
* X axis points to the right (X is width)
* Y axis points down (Y is height)
* Z axis points out of the screen
* A positive rotation thus rotate the image counterclockwise

### Memory Allocation and element access
Allocation and access is almost always done in the order of (y, x), or equivalently, (h, w) and (row, col).
```python
img = np.zeros((480, 640, 3), dtype="uint8")  # creates a 640w by 480h black image
```
```c++
cv::Mat img(480, 640, CV_8CU3, cv::Scalar(0, 0, 0))  // creates a 640w by 480h black image
```
**The only exceptons seem to be when specifying size using `cv::size()`, cv::Rect() and their equivalent in Python** - specify **(x, y)** for these.

## Basic Image Operations
### Translation
```python
M = np.float32([[1, 0, 25],[0, 1, 50]])  # M is the top 2 rows of a 3D homogeneous transformation matrix
size = (img.shape[1], img.shape[0])  # size(w, h) of destination image, same as source img
img = cv2.warpAffine(img, M, size)  # shift img 25 pixels to the right, 50 pixels down
```
### Rotation
```python
(h, w) = img.shape[:2]
center = (w // 2, h // 2)
a = 45  # positive, ccw rotation
scale = 1
# calculate the rotation matrix
# rot = [R | t] where R =  [cos(a), sin(a); -sin(a), cos(a)]; t = center' - R * center'
rot = cv2.getRotationMatrix2D(center, a, scale)
img = cv2.warpAffine(ig, rot, (w, h))
```
### Image arithmetic
OpenCV provided arithmetic operation on `8UC3` matrices clips so that numbers are always in [0, 255]; Numpy operations would wrap around such that 256 = 0

## Histogram
Refer to `hist.py` in the src folder

## Smootiong and Blurring
* Gaussian Blur: intensity of pixels in the neighborhood  are multiplied by a weight inversely proportional to the distence to the center of the neighborhood
* Median Blur: good for removing salt-and-pepper kind of noise
* Bilateral filter: one Gaussian distribution for spatial proximity, another for similarity in intensity -> pixels that are close to the center and has similar intensity to the center pixel gets more weight
## Thresholding
Convert to grayscale -> blur -> threshold
* Simple thresholding: supply a global upper bound and lower bound
* Adaptive thresholding: does thresholding on small sub-images. Could use either mean thresholding or Gaussian (weighte mean) thresholding.
* Otsu's method: **assumes that there are two peaks in the grayscale histogram of the image.** Then tries to find an optimal value to separate the two peaks.

## Gradients and Edge detection
Convert to grayscale -> blur -> find gradient -> non-maximum suppression -> hysteresis thresholding
* **Use `CV_64F`** to store the gradient image!
* Sobel edge detector: compute edge like features along X and Y, and `bitwise_or`ing the Sobel gradient representations
* Canny edge detector: takes in two thresholds values for the gradients, and performs connected component analysis in additional to the above edge detection pipeline.
* see `src/auto_canny.py` for an example of automatic canny edge detector using the median of the image.

## Finding contours
Contours: a curve of points with no gaps in the curve

## Object Detection
## Histogram of Oriente Gradients


## Further Reading
* [OpenCV Cheatsheet](http://docs.opencv.org/2.4/opencv_cheatsheet.pdf) (for 2.4, but most stuff will work for 3)
*
