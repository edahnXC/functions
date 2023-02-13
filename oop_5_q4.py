emp_name=input("Enter the name of employee:")
emp_salary=int(input("Enter the salary of employee per day:"))
days=int(input("Enter the number of working days: "))
class Employee:
    def __init__(self,emp_name,emp_salary):
        self.emp_name=emp_name
        self.emp_salary=emp_salary

    def __mul__(self,other):
        return self.emp_salary * other.days

class workingdays:
    def __init__(self,days):
        self.days=days
    
e=Employee(emp_name,emp_salary)
w=workingdays(days)
print(f"Monthly salary:{e*w}")

    