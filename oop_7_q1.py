from abc import ABC, abstractmethod
 
class Polygons(ABC):
    def __init__(self,sides):
        self.sides=sides

    @abstractmethod
    def get_area(self):
        pass
class Rectangle(Polygons):
    def __init__(self,length,breadth):
        super().__init__(4)
        self.length=length
        self.breadth=breadth

    def get_area(self):
        return self.length*self.breadth
    
class Triangle(Polygons):
    def __init__(self,base,height):
        super().__init__(3)
        self.base=base
        self.height=height

    def get_area(self):
        return 1/2*self.base*self.height
    
rect=Rectangle(5,4)
tri=Triangle(4,8)

print("Area of rectangle=",rect.get_area())
print("Area of Traingle=",tri.get_area())