import cv2
import numpy as np

cap = cv2.VideoCapture(0) #my webcam
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(300,200))
while True:

    ret,frame = cap.read()
    out.write(frame)
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #turning my video to gray
    cv2.imshow("webcam",img_gray)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()