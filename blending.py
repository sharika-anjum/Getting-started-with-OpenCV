import cv2

img1 = cv2.imread("ranvir.jpg")
img2 = cv2.imread("ranbeer.jpg")

result = cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow("result",result)
cv2.waitKey(0)