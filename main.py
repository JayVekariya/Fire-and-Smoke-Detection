import cv2
import numpy as np
import playsound

Fire_report=0;

Alarm_status=False

def alert():
           playsound.playsound('')

video=cv2.VideoCapture('fire2.jpg')
lower = [18, 50, 50]
upper = [35, 255, 255]
lower_smoke = [105, 1, 150]
upper_smoke = [110, 50, 255]

while True:
    ret,frame=video.read()

    if ret == False:
        break

    frame=cv2.resize(frame,(700,400))

    blur=cv2.GaussianBlur(frame,(11,11),0)

    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lower=np.array(lower,dtype='uint8')
    upper=np.array(upper,dtype='uint8')

    lower_smoke = np.array(lower_smoke, dtype='uint8')
    upper_smoke = np.array(upper_smoke, dtype='uint8')

    smoke_mask = cv2.inRange(hsv, lower_smoke, upper_smoke)

    mask=cv2.inRange(hsv,lower,upper)

    cv2.imshow('frame', frame)
    cv2.waitKey(0)

    cv2.imshow('hsv',blur)
    cv2.waitKey(0)

    cv2.imshow('output',mask)
    cv2.waitKey(0)

    size = cv2.countNonZero(mask)

    size_smoke=cv2.countNonZero(smoke_mask)

    print(size_smoke,size)

    if size >= 10000 or size_smoke >=5000:
             Fire_report=1

    if Fire_report>=1:
        if Alarm_status==False :
            alert()
            Alarm_status=True

            if cv2.waitKey(1) == 13:
                break

cv2.waitKey(0)
cv2.destroyAllWindows()
