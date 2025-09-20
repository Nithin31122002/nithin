class Student:
    school_name = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display_info(self):
        print(f"Student: {self.name}, Marks: {self.marks}, School: {Student.school_name}")

    @staticmethod
    def welcome():
        print("Welcome to the Student Portal!")

s1 = Student("Nithin", 85)
s2 = Student("Kumar", 90)

s1.display_info() 
s2.display_info()

Student.welcome()

print("School (via class):", Student.school_name)
print("School (via object):", s1.school_name)
Student.school_name = "XYZ International School"

print("\nAfter changing school_name:")
s1.display_info()
s2.display_info()
