import cv2
print(cv2.__version__)
dispW=320
dispH=240
flip=0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
camSet1='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
Picam1= cv2.VideoCapture(camSet)
Picam2= cv2.VideoCapture(camSet1)
#cam= cv2.VideoCapture(1)
while True:
    ret, frame=Picam1.read()
    ret, frame2=Picam2.read()
    cv2.imshow('piCam1',frame)
    cv2.imshow('piCam2',frame2)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()