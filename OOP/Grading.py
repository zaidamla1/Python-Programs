class Student:
    def __init__(self,name,rollNumber,marks):
        self.name = name
        self.rollNumber = rollNumber
        self.marks = marks

    def add_mark(self,score):
        self.score = score
        for i in self.marks:
            self.score += i
        return self.score
    
    def calculate_average(self):
        self.average = self.score / 3
        return self.average
    
    def get_final_grade(self):
        if self.average > 80:
            print("A grade")
        elif self.average > 60:
            print("B grade")
        elif self.average > 40:
            print("C grade")
        elif self.average >= 33:
            print("D grade")
        else:
            print("F grade 🍕")
        
sub1 = int(input("Enter marks of english"))
sub2 = int(input("Enter marks of maths"))
sub3 = int(input("Enter marks of science"))

s1 = Student("Manish", 12,[sub1,sub2,sub3])
print(s1.add_mark(0))
print(s1.calculate_average())
s1.get_final_grade()        