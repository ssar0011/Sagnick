class Point:
    
    def __init__(self,x,y):
        self.xCoord = x
        self.yCoord = y
        
    def __str__(self):
        return "("+str(self.xCoord)+","+str(self.yCoord)+")"
        
    def __sub__(self,other):
        xDiff = (self.xCoord - other.xCoord)
        yDiff = (self.yCoord - other.yCoord)
        return (xDiff**2 + yDiff**2)**(1/2)

class Line:
    def __init__(self,point1,point2):
        assert type(point1) == type(Point(0,0))
        assert type(point2) == type(Point(0,0))
        self.start = point1
        self.end = point2
    
    def magnitude(self):
        return (float(abs(self.start.xCoord - self.end.xCoord))**2 + float(abs(self.start.yCoord - self.end.yCoord))**2)**(1/2)
		#alternative definition based on Point class's sub method
		#return self.end - self.start
        
    def __str__(self):
        return "<"+str(self.start)+"---"+str(self.end)+">"

P = Point(1,2)
Q = Point(2,4)


L = Line(P,Q)
print(L)
print(L.magnitude())
print(P-Q)


print(P,Q)

P.x = 20

print(P,Q)

P.xCoord = 20

print(P,Q)

Point.yCoord = 100

Point.message = "Ethan was asleep I'm sure"

print(P,Q)

print(Point.message)

print(P.message)
