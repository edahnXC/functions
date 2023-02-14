#2-
from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def message(self):
        pass

class Firstsubclass(Parent):
    def message(self):
        print("This is the first sub class")
    
class Secondsubclass(Parent):
    def message(self):
        print("This is the second subclass")

f1=Firstsubclass()
s1=Secondsubclass()
f1.message()
s1.message()