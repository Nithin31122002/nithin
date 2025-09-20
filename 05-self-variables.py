class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Hello, my name is", self.name)

s1 = Student("Ajay")
s1.show()
s2 = Student("Vijay")
s2.show()   