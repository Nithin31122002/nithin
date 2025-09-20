class Person:
    def __init__(self, name, age):
       
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


p1 = Person("Asha", 21)
p1.show()  

p2 = Person("Rohit", 30)
p2.show() 
