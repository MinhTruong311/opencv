import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    '''lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)'''

    #tra xác định ngưỡng màu hsv để tìm màu
    #các mã màu theo bảng hsv not rgb

    lower_orange = np.array([15,0,0])
    upper_orange = np.array([30, 255, 255])

    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    #cv2.imshow('frame', hsv)
    cv2.imshow('frame', result)   #in ra màu sau khi lọc
    cv2.imshow('mask', mask)  #in ra mask màu trắng đen



    if cv2.waitKey(1) == ord('q'):
        break
cap.realease()
cv2.destroyAllWindows()   