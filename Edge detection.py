import cv2

img = cv2.imread("static/airplane.png")

vert = cv2.Sobel(img,-1,1,0)

hort = cv2.Sobel(img,-1,0,1)

both = cv2.addWeighted(vert,0.5,hort,0.2,0)

cv2.imshow("vertical",vert)
cv2.imshow("horizontal",hort)
cv2.imshow("both",both)
cv2.imshow("actual",img)

cv2.waitKey(0)