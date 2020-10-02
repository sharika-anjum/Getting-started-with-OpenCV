import cv2
import numpy as np



first = np.zeros((512,512),np.uint8)
cv2.circle(first,(200,200),150,(255,255,255),-1)

second = np.zeros((512,512))
cv2.circle(second,(300,300),150,(255,255,255),-1)

imgor = cv2.bitwise_or(first,second) #union
imgand = cv2.bitwise_and(first,second) #intersection
imgxor = cv2.bitwise_xor(first,second) #cuts the common area
imgnot = cv2.bitwise_not(first) #opposite happens

final = np.hstack((first,second))
final1 = np.hstack((first,second,imgor))
final2 = np.hstack((first,second,imgand))
final3 = np.hstack((first,second,imgxor))
final4 = np.hstack((first,imgnot))

cv2.imshow("image",final)
cv2.imshow("OR",final1)
cv2.imshow("AND",final2)
cv2.imshow("XOR",final3)
cv2.imshow("NOT",final4)
cv2.waitKey(0)