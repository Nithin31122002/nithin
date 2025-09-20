class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0


# Usage
print("Addition:", MathOperations.add(10, 20))      # 30
print("Is 10 even?", MathOperations.is_even(10))    # True
print("Is 7 even?", MathOperations.is_even(7))      # False