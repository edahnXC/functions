from abc import ABC, abstractmethod

class Marks(ABC):
    @abstractmethod
    def get_percentage(self):
        pass

class A(Marks):
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def get_percentage(self):
        return (self.m1 + self.m2 + self.m3) / 3

class B(Marks):
    def __init__(self, m1, m2, m3, m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
    
    def get_percentage(self):
        return (self.m1 + self.m2 + self.m3 + self.m4) / 4
    
a = A(70, 80, 90)
b = B(70, 80, 90, 80)

print("Percentage of A:", a.get_percentage())
print("Percentage of B:", b.get_percentage())
