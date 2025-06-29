# Examples of __init__ in practice

# First, let's import your Solution class
from add_two_numbers import Solution

def test_your_solution():
    """Test your add_two_numbers Solution class"""
    print("TESTING YOUR ADD_TWO_NUMBERS SOLUTION")
    print("=" * 50)
    
    # Example 1: Basic usage
    print("Example 1: Basic Usage")
    l1 = [2, 4, 3]  # represents 342
    l2 = [5, 6, 4]  # represents 465
    
    print(f"Creating Solution({l1}, {l2})")
    solution = Solution(l1, l2)  # This calls __init__ automatically
    print(f"Result: {solution.funct()}")  # Should be 807
    
    # Example 2: Show what __init__ created
    print(f"\nWhat __init__ set up:")
    print(f"  len1: {solution.len1}")
    print(f"  len2: {solution.len2}")
    print(f"  re_l1: {solution.re_l1}")
    print(f"  re_l2: {solution.re_l2}")

# Example 1: Bank Account
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        print(f"Account {account_number} created with balance ${initial_balance}")
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

# Example 2: Student (like your learningclass.py)
class Student:
    count = 0  # Class variable
    
    def __init__(self, name, age, gpa):
        self.name = name      # Instance variables
        self.age = age
        self.gpa = gpa
        Student.count += 1    # Update class variable
        print(f"Student {name} enrolled!")
    
    def study(self, hours):
        print(f"{self.name} studied for {hours} hours")

# Example 3: Calculator (maintains state)
class Calculator:
    def __init__(self):
        self.result = 0       # Starting value
        self.history = []     # Keep track of operations
    
    def add(self, x):
        self.result += x
        self.history.append(f"Added {x}")
        return self.result
    
    def multiply(self, x):
        self.result *= x
        self.history.append(f"Multiplied by {x}")
        return self.result

# Usage examples:
if __name__ == "__main__":
    # Test your add_two_numbers solution
    test_your_solution()
    
    print("\n" + "=" * 60)
    print("OTHER __init__ EXAMPLES:")
    print("=" * 60)
    
    # Example 1: Bank Account usage
    print("\nBank Account Example:")
    account1 = BankAccount("12345", 100)
    account1.deposit(50)
    print(f"Account balance: ${account1.balance}")
    
    # Example 2: Student usage  
    print("\nStudent Example:")
    student1 = Student("Alice", 20, "Computer Science")
    student1.add_grade(95)
    student1.add_grade(87)
    print(f"Student info: {student1.get_info()}")
    
    # Example 3: Car usage
    print("\nCar Example:")
    car1 = Car("Toyota", "Camry", 2020)
    car1.start()
    car1.drive(50)
    print(f"Car odometer: {car1.odometer} miles")
