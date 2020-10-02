import cv2
import numpy as np

img = cv2.imread("static/baboon.jpg")

mask1 = np.ones(img.shape,np.uint8)*50

result1 = cv2.add(img,mask1) #bright
result2 = cv2.subtract(img,mask1) #dark
final = np.hstack((result2,img,result1))
cv2.imshow("image",final)
cv2.waitKey(0)

