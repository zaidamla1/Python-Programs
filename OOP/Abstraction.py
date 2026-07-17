#abstract class : a class that contains at least one abstract method. It can also contain not abstract method

#abstract method : a method that does have it's own code block it needs to be overriden in child class compulsorily.

from abc import ABC,abstractmethod

class Employee(ABC):

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @abstractmethod
    def empDetails(self):
        pass

    @abstractmethod
    def hello(self):
        pass

    def welcome(self):
        print("Welcome to our Company")


class Employee1(Employee):

    def __init__(self, name, salary,gender):
        super().__init__(name, salary)
        self.gender = gender

    def hello(self):
        print("Hello Employees")

    def empDetails(self):
        print(f"Name of employee {self.name}")
        print(f"Salary of employee {self.salary}")
        print(f"Gender of employee {self.gender}")


e1 = Employee1("Manish",15000,"male")
e1.hello()
e1.welcome()
e1.empDetails()






