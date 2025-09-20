class Student:
    school_name = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"{self.name} studies at {Student.school_name} and scored {self.marks} marks.")
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
s1 = Student("Nithin", 85)
s2 = Student("Kumar", 90)

print("Before modification:")
s1.show()
s2.show()
Student.school_name = "XYZ International School"

print("\nAfter modification (via class name):")
s1.show()
s2.show()
Student.change_school("Global Public School")

print("\nAfter modification (via class method):")
s1.show()
s2.show()
