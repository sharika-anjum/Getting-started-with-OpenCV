import numpy as np
import cv2

img = cv2.imread("static/airplane.png")

first = np.zeros((512,512,3),np.uint8)
cv2.circle(first,(200,200),150,(255,255,255),-1)

imgAnd = cv2.bitwise_xor(img,first)

final = np.hstack((img,first,imgAnd))

cv2.imshow("image",final)
cv2.waitKey(0)
