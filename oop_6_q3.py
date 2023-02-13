class Engine:
    a = 0       #static variable
    def __init__(self, b):
        self.b = b           #instance variable
        
    def m1(self):
        print("This is Engine class method....")
        
class Car:
    def __init__(self, engine):
        self.engine = engine
        
    def m2(self):
        print("Instance Variable b:", self.engine.b)
        self.engine.m1()
        
car = Car(Engine(10))
car.m2()
