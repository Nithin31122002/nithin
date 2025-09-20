class Student:
    school_name = "MET School"   # class variable (static variable)

    def __init__(self, name):
        self.name = name         # instance variable

    @classmethod
    def get_school_name(cls):
        # Access class variable using cls
        return cls.school_name


# Usage
s1 = Student("Nithin")
s2 = Student("Kumar")

print("Student 1:", s1.name)
print("Student 2:", s2.name)

# Access class method
print("School Name:", Student.get_school_name())
