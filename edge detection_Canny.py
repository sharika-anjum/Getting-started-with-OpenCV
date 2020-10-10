import cv2


def sketch(img):
    # to convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray,(5,5),10)
    both = cv2.Canny(blur,10,70)

    ret, bw = cv2.threshold(both, 127, 255, cv2.THRESH_BINARY)
    return bw


cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    cv2.imshow("Webcam", sketch(frame))

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()