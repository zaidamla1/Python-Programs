class Garage:
    def __init__(self,name,address,regNumber):
        self.name = name
        self.address = address
        self.regNumber = regNumber


class Brand(Garage):
    def __init__(self, name, address, regNumber, logo,revenue):
        super().__init__(name, address, regNumber)
        self.logo = logo
        self.revenue = revenue
    
class Showroom(Brand):
    def __init__(self, name, address, regNumber, logo, revenue,franchise, customerCare):
        super().__init__(name, address, regNumber, logo, revenue)
        self.franchise = franchise
        self.customerCare = customerCare
    
    def details(self):
        print(f"Name of Showroom {self.name}")
        print(f"Address of Showroom {self.address}")
        print(f"Govt Regestration Id is {self.regNumber}")
        print(f"Logo refined {self.logo}")

s1 = Showroom("IICL Motors", "Majura Gate", "REG-0001", "IICL India",1500,"Dindoli",9876543121)
s1.details()

        