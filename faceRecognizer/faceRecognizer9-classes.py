class Rectangle:
    def __init__(self,w,l,c):
        self.width=w
        self.length=l
        self.color=c
    def area(self): #use .area() to call this function
        self.area=self.width*self.length
        return self.area 
    def per(self): #use .per() to calll this function
        self.perimeter=2*(self.width + self.length)
        return self.perimeter

w1=3
l1=4
c1="red"
rect1=Rectangle(l1,w1,c1)
areaRect1=rect1.area()
perRect1=rect1.per()
print("Area of rectangle 1 is: ",areaRect1)
#print("Rectangle 1 is",rect1.color,"with length",rect1.length,"with width",rect1.width,"and area is:",rect1.area)

w2=10
l2=10
c2="blue"
rect2=Rectangle(l2,w2,c2)
areaRect2=rect2.area()
perRect2=rect2.per()
print("Area of rectangle 2 is: ",areaRect2,"The color of the rectangle is :",rect2.color,"\n Perimeter of rectangle 2 is:",perRect2)