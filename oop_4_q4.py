class Person:
    class DOB:
        def __init__(self,dd,mm,yyyy):
            self.dd=dd
            self.mm=mm
            self.yyyy=yyyy

        def display(self):
            return f"{self.dd}/{self.mm}/{self.yyyy}"

    def __init__(self,name,day,month,year):
        self.name=name
        self.dob=self.DOB(day,month,year)

    def display(self):
        return f"Name of the person is:{self.name}\nDOB:{self.dob.display()}"

P=Person("rahul",12,1,2003)
print(P.display())            