class Student:
    school_name = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}, School: {Student.school_name}")


s1 = Student("Nithin", 85)
s2 = Student("Kumar", 90)
print("School (via class):", Student.school_name)
print("School (via object):", s1.school_name)

s1.display()
s2.display()
Student.school_name = "MET School"

print("\nAfter changing static variable:")
s1.display()
s2.display()
