import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=0
#Uncomment These next Two Line for Pi Camera
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
#cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    frame=cv2.rectangle(frame,(340,100),(450,190),(0,255,0),-3)
    frame=cv2.circle(frame,(320,240),50,(255,255,255),5)
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame,'My first text',(300,300),fnt,1.5,(255,0,150),2)
    frame=cv2.line(frame,(10,10),(630,470),(0,0,0),4)
    frame=cv2.arrowedLine(frame,(10,470),(630,10),(255,255,255),1)
    cv2.imshow('nanoCam',frame)
    cv2.moveWindow('nanoCan',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()