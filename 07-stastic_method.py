class Bank:

    @staticmethod
    def calculate_interest(principal, rate, time):
        """Simple Interest Formula: (P * R * T) / 100"""
        return (principal * rate * time) / 100

    @staticmethod
    def bank_policy():
        print("Bank Policy: Minimum balance should be ₹1000.")
Bank.bank_policy()

si = Bank.calculate_interest(10000, 5, 2)
print("Simple Interest:", si)
obj = Bank()
print("Interest via object:", obj.calculate_interest(5000, 7, 1))
