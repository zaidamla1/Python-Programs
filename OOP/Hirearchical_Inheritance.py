class Employee:
    def __init__(self,name,salary,workingHours):
        self.name = name
        self.salary = salary
        self.workingHours = workingHours
    
    def details(self):
        print(f"Name of employee is {self.name}")
        print(f"Salary of employee is {self.salary}")
        print(f"Working hours is {self.workingHours}")


class Manager(Employee):
    def __init__(self, name, salary, workingHours,exp):
        super().__init__(name, salary, workingHours)
        self.exp = exp
    
    def details(self):
        print(f"Name of manager is {self.name}")
        print(f"Salary of manager is {self.salary}")
        print(f"Working hours is {self.workingHours}")
        


class HR(Employee):
    def __init__(self, name, salary, workingHours, reportingTo):
        super().__init__(name, salary, workingHours)
        self.reportingTo = reportingTo

    def details(self):
        print(f"Name of HR {self.name}")
        print(f"Salary of HR {self.salary}")
        print(f"Working hours of HR {self.workingHours}")

m1 = Manager("Manish",90000,10,3)
m1.details()
print()
h1 = HR("Sakshi",75000,10,"Kenil")
h1.details()
