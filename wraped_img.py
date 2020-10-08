import numpy as np
import cv2

img = cv2.imread("static/airplane.png")
click = 0
pt1x = pt1y = pt2x = pt2y = pt3x = pt3y = pt4x = pt4y = 0
def draw(event,x,y,flag,params):

    global click,pt1x,pt1y,pt2x,pt2y,pt3x,pt3y,pt4x,pt4y
    if event == cv2.EVENT_LBUTTONDOWN:

        click += 1
        cv2.circle(img,(x,y),5,(0,0,255),-1)

        if(click%4==1):
            pt1x = x
            pt1y = y

            print("1st coordinate is ({},{})".format(pt1x,pt1y))

        if (click % 4 == 2):
            pt2x = x
            pt2y = y

            print("2nd coordinate is ({},{})".format(pt2x, pt2y))

        if (click % 4 == 3):
            pt3x = x
            pt3y = y

            print("3rd coordinate is ({},{})".format(pt3x, pt3y))

        if (click % 4 == 0):
            pt4x = x
            pt4y = y

            print("4th coordinate is ({},{})".format(pt4x, pt4y))

            point1 = np.float32([[pt1x,pt1y],[pt2x,pt2y],[pt3x,pt3y],[pt4x,pt4y]])

            width = abs(pt2y - pt1y) *2
            height = abs(pt3x - pt1x) *2

            point2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

            matrix = cv2.getPerspectiveTransform(point1,point2)
            output = cv2.warpPerspective(img,matrix,(width,height))

            cv2.imshow("Warped",output)
            cv2.waitKey(0)

cv2.namedWindow(winname = "image")
cv2.setMouseCallback("image",draw)

while True:

    cv2.imshow("image",img)

    if cv2.waitKey(1)  & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
