import cv2
import numpy as np
import time

print(cv2.__version__)
dispW=640
dispH=480
flip=0
sec=0 
font=cv2.FONT_HERSHEY_SIMPLEX
dtav=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc sensor_id =0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
camSet1='nvarguscamerasrc sensor_id =1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam1= cv2.VideoCapture(camSet)
cam2= cv2.VideoCapture(camSet1)
startTime=time.time()
#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(2)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame1 = cam1.read()
    ret, frame2 = cam2.read()
    print(frame1.shape)
    #frame2=cv2.resize(frame2,(640,480))
    #frame2=cv2.resize(frame2,(frame1.shape[1],frame1.shape[0]))
    frameCombined=np.hstack((frame1,frame2))
    dt=time.time()-startTime
    startTime=time.time()
    dtav=.9*dtav+.1*dt
    fps=1/dtav  
    cv2.rectangle(frameCombined,(0,0),(130,40),(0,0,255),-1)
    cv2.putText(frameCombined,str(round(fps,1))+'FPS:',(0,25),font,0.75,(0,255,255),2)
    cv2.imshow('Combo',frameCombined)
    cv2.moveWindow('Combo',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()