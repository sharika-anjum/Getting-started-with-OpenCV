import numpy as np
import cv2

img = cv2.imread("static/airplane.png",0) #this will automatically show the grayscale image

ret, thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
ret1, thresh2  = cv2.threshold(img,200,255,cv2.THRESH_BINARY_INV)
ret2, thresh3 = cv2.threshold(img,200,255,cv2.THRESH_TRUNC)
ret3, thresh4 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO)
ret4, thresh5 = cv2.threshold(img,200,255,cv2.THRESH_TOZERO_INV)

final = np.hstack((thresh4,thresh5))
cv2.imshow("image",final)
cv2.waitKey(0)


