# Method Overriding : Same name of methods with same parameters, in different class with inheritance.



class Demo:

    def test(self):
        print("Test-1")

class Main(Demo):
    def test(self):
        print("Test-2")



m = Main()
m.test()