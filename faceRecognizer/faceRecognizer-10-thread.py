from threading import Thread
import time
def BigBox(color,l):
    while True:
        print(color,"Box is Open of length",l)
        time.sleep(5)
        print(color,"Box is Closed of length",l)
        time.sleep(5)
def SmallBox(color,l):
    while True:
        print(color,"box is open of length",l)
        time.sleep(1)
        print(color,"box is closed of length",l)
        time.sleep(1)
x=5
bigBoxThread=Thread(target=BigBox,args=("red",x))
x=4
smallBoxThread=Thread(target=SmallBox,args=("blue",x))
bigBoxThread.daemon=True
smallBoxThread.daemon=True
bigBoxThread.start()
smallBoxThread.start()
while True:
    pass