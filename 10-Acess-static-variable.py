class Student:
    school_name = "ABC School"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(f"{self.name} studies at {Student.school_name} and scored {self.marks} marks.")
print("Access via Class:", Student.school_name)
s1 = Student("Nithin", 85)
s2 = Student("Kumar", 90)

print("Access via Object (s1):", s1.school_name)
print("Access via Object (s2):", s2.school_name)
s1.show()
s2.show()
Student.school_name = "DONBOSCO School"

print("\nAfter changing static variable:")
s1.show()
s2.show()
