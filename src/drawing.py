import cv2
import numpy as np
# import random
if __name__ == "__main__":
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    green = (0, 255, 0)
    red = (0, 0, 255)
    blue = (255, 0, 0)
    """
    cv2.line(canvas, (0, 0), (300, 300), green, lineType=cv2.LINE_AA)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)
    cv2.line(canvas, (300, 0), (0, 300), red, 3)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)
    cv2.rectangle(canvas, (10, 10), (60, 60), green)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)
    cv2.rectangle(canvas, (50, 200), (20, 225), red, 5)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)
    cv2.rectangle(canvas, (200,50), (225, 125), blue, -1, cv2.LINE_AA)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

    canvas = np.zeros((300, 300, 3), dtype="uint8")
    (cX, cY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)  # floor divide to round
    white = (255, 255, 255);
    for r in range(0, cX, 25):
        cv2.circle(canvas, (cX, cY), r, white, lineType=cv2.LINE_AA)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)
    """
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    for i in range(0, 30, 1):
        for j in range(0+(i+1)%2, 30, 2):
            canvas[i*10:(i+1)*10-1, j*10:(j+1)*10-1] = red
    cv2.circle(canvas, (150, 150), 50, green, -1, lineType=cv2.LINE_AA)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)
    canvas = np.zeros((300, 300, 3), dtype="uint8")

    for i in range(0, 25):
        radius = np.random.randint(5, high=200);
        color = np.random.randint(0, high=255, size=(3,)).tolist()
        pt = np.random.randint(0, high=300, size=(2,))
        cv2.circle(canvas, tuple(pt), radius, color, -1)
    cv2.imshow("canvas", canvas)
    cv2.waitKey(0)

