import cv2
import numpy as np

x = np.full((500,800),255,dtype=np.uint8)


cv2.imshow("abc", x )
cv2.waitKey(0)