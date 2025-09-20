class Student:
    school_name = "ABC School" 
    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks

    def display_info(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"School name changed to: {cls.school_name}")

    @staticmethod
    def welcome():
        print("Welcome to the Student Management System!")

s1 = Student("Nithin", 85)
s1.display_info()
Student.change_school("XYZ International School")
Student.welcome()
