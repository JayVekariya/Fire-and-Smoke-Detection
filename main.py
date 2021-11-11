import cv2
import numpy as np
import playsound

Fire_report=0;

Alarm_status=False

def alert():
           playsound.playsound('alarm.wav')

video=cv2.VideoCapture('Smoke1.jpg')

lower_fire = [18, 50, 50]
upper_fire = [35, 255, 255]

lower_smoke = [105, 1, 150]
upper_smoke = [110, 50, 255]

while True:
    ret,frame=video.read()

    if ret == False:
        break

    frame=cv2.resize(frame,(700,400))

    blur=cv2.GaussianBlur(frame,(11,11),0)

    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lower_fire=np.array(lower_fire, dtype='uint8')
    upper_fire=np.array(upper_fire, dtype='uint8')

    lower_smoke = np.array(lower_smoke, dtype='uint8')
    upper_smoke = np.array(upper_smoke, dtype='uint8')

    smoke_mask = cv2.inRange(hsv, lower_smoke, upper_smoke)

    fire_mask=cv2.inRange(hsv,lower_fire,upper_fire)

    cv2.imshow('frame', frame)
    cv2.waitKey(0)

    cv2.imshow('hsv',blur)
    cv2.waitKey(0)

    cv2.imshow('output_Fire',fire_mask)
    cv2.waitKey(0)

    cv2.imshow('output_Smoke',smoke_mask)
    cv2.waitKey(0)

    size_fire = cv2.countNonZero(fire_mask)

    size_smoke=cv2.countNonZero(smoke_mask)

    print(size_smoke,size_fire)

    if size_fire >= 10000 or size_smoke >=5000:
             Fire_report=1

    if Fire_report == 1:
        if Alarm_status==False :
            alert()
            Alarm_status=True

            if cv2.waitKey(1) == 13:
                break

def alert():
    playsound.playsound('')

cv2.waitKey(0)
cv2.destroyAllWindows()
