import numpy as np
import cv2

img = cv2.imread("static/airplane.png",0)

thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,5)
thresh1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)


cv2.imshow("image",thresh)
cv2.imshow("image",thresh1)
cv2.waitKey(0)