# Notes
## Notations and conventions
### Coordinate system
OpenCV uses a coordinate system defined as follows:

* The origin of the coordinate system is on the top left corner of the image
* X axis points to the right
** X is width
* Y axis points down
** Y is height
* Z axis points out of the screen
** A positive rotation thus rotate the image counterclockwise

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

### Histogram
Refer to `hist.py` in the src folder


### Smootiong and Blurring


## Further Reading
* [OpenCV Cheatsheet](http://docs.opencv.org/2.4/opencv_cheatsheet.pdf)(for 2.4, but most stuff will work for 3)
*
