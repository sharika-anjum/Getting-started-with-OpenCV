import numpy as np
import cv2

flag = False
ix = -1
iy = -1

def draw(event,x,y,flags,params):
    global flag,ix,iy

    if event == 1: #click
        flag = True
        ix=x
        iy=y

    elif event == 0: #drag
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(0,255,255),thickness=-1)

    else: 
        flag=False
        cv2.rectangle(img, pt1=(ix, iy), pt2=(x, y), color=(0, 255, 255), thickness=-1)
cv2.namedWindow(winname = "window")
cv2.setMouseCallback("window",draw)

img = np.zeros((512,512,3))

while True:

    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()