class Employee:
    def __init__(self,empId,empName,empSalary):
        self.empId = empId
        self.empName = empName
        self.empSalary = empSalary

    def printDetails(self, empGender):
        print(f"Employee id :- {self.empId}")
        print(f"Employee name :- {self.empName}")
        print(f"Empployee salary :- {self.empSalary}")
        print(f"Employee gender :- {empGender}")

    def calculateSalary(self,dayWorked):
        netSalary = self.empSalary / 30 * dayWorked;
        print(netSalary)


e1 = Employee("E-001","Manish",25000)
e1.printDetails("male")
e1.calculateSalary(25)
e2 = Employee("E-002", "Mukesh", 28000)
e2.printDetails("male")
e2.calculateSalary(12)
        