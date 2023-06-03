def RectCalc(w,l):
    area=w*l
    perimeter=2*(w+l)
    return area,perimeter

l1=3
w1=5
area1,perimeter1= RectCalc(w1,l1)
print("Rectangle1 area is:",area1,perimeter1)
l2=6
w2=4
area2,perimeter2= RectCalc(w2,l2)
print("Rectangle2 area is:",area2,perimeter2)