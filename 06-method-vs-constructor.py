class Student:
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        print("Constructor is called. Student object created!")


    def show_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


s1 = Student("Nithin", 20)
s1.show_details()
