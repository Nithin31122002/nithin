class Outer:
    def __init__(self, name):
        self.name = name   # instance variable

    class Inner:
        def __init__(self, outer_obj):
            self.outer = outer_obj   # store outer class object

        def display(self):
            # Access outer instance variable
            print("Outer Instance Variable:", self.outer.name)


# Usage
outer = Outer("Nithin")        # Create outer object
inner = outer.Inner(outer)     # Pass outer object to inner
inner.display()
