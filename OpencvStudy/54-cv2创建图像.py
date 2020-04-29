import numpy as np
import cv2

img = np.zeros([300, 600, 3])

img[:, :, 0] = np.ones([300, 600]) * 255
print(img[:, :, 0])
print("-----------------------------")
img[:, :, 1] = np.ones([300, 600]) * 100
print(img[:, :, 1])
print("-----------------------------")
img[:, :, 2] = np.ones([300, 600]) * 0
print(img[:, :, 2])
print("-----------------------------")

cv2.imshow("test", img)

cv2.waitKey(0)
