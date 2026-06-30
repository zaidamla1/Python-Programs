class Parent:
    def __init__(self, surName,fees):
        self.surName = surName
        self.fees = fees

class Child (Parent):
    def __init__(self,surName,fees,name,std):
        super().__init__(surName,fees)
        self.name = name
        self.std = std

    def printDetails(self):
        print(f"Surname of Child :- {self.surName}")
        print(f"Name of Child :- {self.name}")
        print(f"Standard of Child :- {self.std}")
        print(f"Annual fees Child :- {self.fees}")
        

p1 = Parent("Mehta",15000)
c1 = Child("Mehta", 12000,"Manish",5)
c1.printDetails()
