import numpy as np
import cv2

img = np.zeros([300, 600, 1], np.uint8)

img[:, :, 0] = np.ones([300, 600]) * 127

cv2.imshow("huise", img)

cv2.waitKey(0)
