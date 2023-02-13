#create a point class that has distance () method which find distance between 2 points. Test with Point1(3,2) and Point2(9,7)

import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def distance(self,other):
        return math.sqrt((other.x-self.x)**2 + (other.y-self.y)**2)

Point1=Point(3,2)
Point2=Point(9,7)
print(Point1.distance(Point2))

