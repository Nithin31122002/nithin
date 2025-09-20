class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Ajay")

s2 = s1
print("s1 name:", s1.name)
print("s2 name:", s2.name)

s2.name = "Vijay"

print("After changing through s2...")
print("s1 name:", s1.name) 
print("s2 name:", s2.name)
