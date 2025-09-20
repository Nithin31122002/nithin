class Outer:
    school_name = "ABC School"   # static variable

    class Inner:
        def show(self):
            # Access static variable of outer class
            print("School:", Outer.school_name)

        def change_school(self, new_name):
            # Modify outer class static variable
            Outer.school_name = new_name
