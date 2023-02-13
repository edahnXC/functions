#to check who has greater marks using > operator
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def __gt__(self,other):
        return self.marks > other.marks
    
student1=Student("Ram",80)
student2=Student("Om",89)

if student1>student2:
    print(student1.name,"has greater marks")
else:
    print(student2.name,"has greater marks")