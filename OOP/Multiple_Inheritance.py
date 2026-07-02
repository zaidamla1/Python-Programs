class Father:
    def __init__(self,surName,schoolFees):
        self.surName = surName
        self.schoolFees = schoolFees
class Mother:
    def __init__(self,pocketMoney,address):
        self.pocketMoney = pocketMoney
        self.address = address
        

class Child(Father,Mother):
    def __init__(self, surName, schoolFees,pocketMoney,address,name,std):
        Father.__init__(self,surName, schoolFees)
        Mother.__init__(self,pocketMoney,address)
        self.name = name
        self.std = std

    def studentDetails(self):
        print(f"Surname of student {self.surName}")
        print(f"Name of student {self.name}")
        print(f"Stadard of student {self.std}")
        print(f"School fees recieved {self.schoolFees}")
        print(f"Pocket money recieved {self.pocketMoney}")

c1 = Child("Mehra",2500,1200,"Bhagal","Manish",7)
c1.studentDetails()