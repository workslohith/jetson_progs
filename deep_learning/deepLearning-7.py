import cv2
import jetson.inference
import jetson.utils
import time
import numpy as np
timeStamp=time.time()
fpsFilt=0
flip= 0

net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)
dispW=1280
dispH=720
font =cv2.FONT_HERSHEY_SIMPLEX
#Gstreamer code 
#camSet='nvarguscamerasrc sensor_id=0 !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam=cv2.VideoCapture(camSet)

#cam=jetson.utils.gstCamera(dispW,dispH,'0') for using the rpi camera
cam=cv2.VideoCapture('/dev/video2')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

#cam= jetson.utils.gstCamera(dispW,dispH,'/dev/video2') #for using the webcam
#display=jetson.utils.glDisplay()
while True:
    #img, width, height= cam.CaptureRGBA()
    _,img = cam.read()
    height=img.shape[0]
    width=img.shape[1]

    frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame=jetson.utils.cudaFromNumpy(frame)

    detections=net.Detect(frame, width, height)
    for detect in detections:
        #print(detect)
        ID=detect.ClassID
        top=int(detect.Top) 
        bottom=int(detect.Bottom) 
        right=int(detect.Right) 
        left=int(detect.Left)
        item=net.GetClassDesc(ID)
        #print(item,top,left,bottom,right)
        tk=1
        if item=='cat':
            tk=-1
        cv2.rectangle(img,(left,top),(right,bottom),(0,255,0),tk)
        cv2.putText(img,item,(left,top+20),font,.75,(255,0,0),2)
    #display.RenderOnce(img,width,height)
    dt=time.time()-timeStamp
    timeStamp=time.time()
    fps=1/dt
    fpsFilt=.9*fpsFilt + .1*fps
    #print(str(round(fps,1))+' fps') #to display in terminal
    cv2.putText(img,str(round(fpsFilt,1))+ ' fps ',(0,30),font,1,(0,0,255),2)
    cv2.imshow('detCam',img)
    cv2.moveWindow('detCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
