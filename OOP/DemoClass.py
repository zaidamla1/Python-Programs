class Human:
    citizen = "IN"

    def __init__(self,name,age,gender):
        self.username = name
        self.age = age
        self.gender = gender
    
        
   


h1 = Human("Manish",25,"male")
print(h1.age)
print(h1.username)
print(h1.gender)
print(h1.citizen)

print()

h2 = Human("Mukesh",23,"male")
print(h2.age)
print(h2.username)
print(h2.gender)
print(h2.citizen)
