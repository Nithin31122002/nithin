class Student:
    school_name = "ABC School"

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name 
        print(f"School name updated to: {cls.school_name}")

s1 = Student("Nithin", 85)
s2 = Student("Kumar", 90)

print("Before changing school:")
print(s1.school_name)  
print(s2.school_name)   

Student.change_school("XYZ International School")

print("\nAfter changing school:")
print(s1.school_name)
print(s2.school_name)
