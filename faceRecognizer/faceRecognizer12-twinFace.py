from threading import Thread
import cv2
import time
import numpy as np
import face_recognition
import pickle

dtav=0
font=cv2.FONT_HERSHEY_SIMPLEX

with open('train.pkl','rb') as f:
    Names=pickle.load(f)
    Encodings=pickle.load(f)

flip=0
dispW=640
dispH=480
camSet='nvarguscamerasrc sensor_id =0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
camSet1='nvarguscamerasrc sensor_id =1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

class vStream:
    def __init__(self,src,width,height):
        self.width=width
        self.height=height
        self.capture=cv2.VideoCapture(src)
        self.thread=Thread(target=self.update,args=())
        self.thread.daemon=True
        self.thread.start()
    def update(self):
        while True:
            _,self.frame=self.capture.read()
            self.frame2=cv2.resize(self.frame,(self.width,self.height))
    def getFrame(self):
        return self.frame2

#camSet='nvarguscamerasrc sensor_id =0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#camSet1='nvarguscamerasrc sensor_id =1 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam1=vStream(camSet,dispW,dispH)
cam2=vStream(camSet1,dispW,dispH)

startTime=time.time()
dtav=0
scaleFactor=.2
while True:
    try:
        myFrame1=cam1.getFrame()
        myFrame2=cam2.getFrame()
        myFrame3=np.hstack((myFrame1,myFrame2))
        frameRGB=cv2.cvtColor(myFrame3,cv2.COLOR_BGR2RGB)
        frameRGBsmall=cv2.resize(frameRGB,(0,0),fx=scaleFactor,fy=scaleFactor)
        facePositions=face_recognition.face_locations(frameRGBsmall,model='cnn')
        allEncodings=face_recognition.face_encodings(frameRGBsmall,facePositions)
        for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
            name="Unknown Person"
            matches=face_recognition.compare_faces(Encodings,face_encoding)
            if True in matches:
                first_match_index=matches.index(True)
                name=Names[first_match_index]
                print(name)
            top=int(top/scaleFactor)
            left=int(left/scaleFactor)
            right=int(right/scaleFactor)
            bottom=int(bottom/scaleFactor)
            cv2.rectangle(myFrame3,(left,top),(right,bottom),(0,0,255),2)
            cv2.putText(myFrame3,name,(left,top-6),font,.75,(0,255,255),2)
            
        dt=time.time()-startTime
        startTime=time.time()
        dtav=.9*dtav+.1*dt
        fps=1/dtav
        cv2.rectangle(myFrame3,(0,0),(100,40),(0,0,255),-1)
        cv2.putText(myFrame3,str(round(fps,1))+ ' fps',(0,25),font,.75,(0,255,255))
        cv2.imshow('comboCam',myFrame3)
        cv2.moveWindow('comboCam',0,0)
        #cv2.imshow("piCam2",myFrame2)
    except:
        time.sleep(5)
        print("frame not available")
    if cv2.waitKey(1)==ord('q'):
        cam1.capture.release()
        cam2.capture.release()
        cv2.destroyAllWindows()
        exit(1)
        break

