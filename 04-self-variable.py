class Student:
    def __init__(self, name, age):
    
        self.name = name
        self.age = age

    def show(self):
    
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Ajay", 20)
s1.show()

s2 = Student("Vijay", 22)
s2.show()
