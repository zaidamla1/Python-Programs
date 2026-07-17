class Employee:
    def __init__(self,name,exp):
        self.name = name  #public
        self._exp = exp   #protected with one underscore
    
    #getter and setter

    def setSalary(self,salary):
        self.__salary = salary
    
    def getSalary(self):
        return self.__salary







e1 = Employee("Manish",5)
e1.name = "Suresh"
e1._exp = 3
e1.__salary = 30000
e1.setSalary(40000)
salary = e1.getSalary()
print(e1.name)
print(e1._exp)
print(e1.__salary)
print(salary)