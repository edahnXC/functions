class Employee:
    def __init__(self,emp_name,emp_department,emp_salary):
        self.emp_name=emp_name
        self.emp_department=emp_department
        self.emp_salary=emp_salary

    def display(self):
        print("Employee name=",self.emp_name)
        print("Employee department=",self.emp_department)
        print("Employee salary=",self.emp_salary)
    
class UpdateEmp(Employee):
    def updateinfo(employee,department,salary):
        employee.emp_department=department
        employee.emp_salary=salary
    
e=Employee("Ram","HR",40000)
e.display()
UpdateEmp.updateinfo(e,"IT",50000)
e.display()