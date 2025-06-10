#!/usr/bin/env python3
"""
Complete demonstration of how __init__ works with your add_two_numbers.py program
"""

from add_two_numbers import Solution

def demonstrate_init_step_by_step():
    """Show exactly what happens when __init__ is called"""
    print("HOW __init__ WORKS WITH YOUR PROGRAM")
    print("=" * 60)
    
    print("Step 1: You write this code:")
    print("    l1 = [2, 4, 3]")
    print("    l2 = [5, 6, 4]")
    print("    solution = Solution(l1, l2)")
    print()
    
    # Actually do it
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    
    print("Step 2: Python automatically calls __init__(self, l1, l2)")
    print("Step 3: Your __init__ method executes:")
    print("    self.len1 = len(l1) = 3")
    print("    self.len2 = len(l2) = 3")
    print("    self.re_l1 = {}")
    print("    self.re_l2 = {}")
    print()
    
    print("Step 4: __init__ reverses the lists:")
    print("    Original l1 = [2, 4, 3] (represents 342)")
    print("    Reversed re_l1 = {0: 3, 1: 4, 2: 2}")
    print("    Original l2 = [5, 6, 4] (represents 465)")
    print("    Reversed re_l2 = {0: 4, 1: 6, 2: 5}")
    print()
    
    # Create the solution
    solution = Solution(l1, l2)
    
    print("Step 5: Object is created and returned")
    print(f"    solution.len1 = {solution.len1}")
    print(f"    solution.len2 = {solution.len2}")
    print(f"    solution.re_l1 = {solution.re_l1}")
    print(f"    solution.re_l2 = {solution.re_l2}")
    print()
    
    print("Step 6: You can now call methods on the object:")
    result = solution.funct()
    print(f"    solution.funct() = {result}")

def test_multiple_objects():
    """Show how each object gets its own __init__ call"""
    print("\n\nMULTIPLE OBJECTS - EACH GETS ITS OWN __init__")
    print("=" * 60)
    
    test_cases = [
        ([1, 2], [3, 4], "12 + 34 = 46"),
        ([9, 9, 9], [1], "999 + 1 = 1000"),
        ([0], [0], "0 + 0 = 0"),
        ([5], [7], "5 + 7 = 12")
    ]
    
    solutions = []
    
    for i, (l1, l2, description) in enumerate(test_cases, 1):
        print(f"Test {i}: Creating Solution({l1}, {l2})")
        solution = Solution(l1, l2)  # Each call creates new object with __init__
        result = solution.funct()
        solutions.append(solution)
        print(f"  {description} -> Result: {result}")
        print(f"  Object's re_l1: {solution.re_l1}")
        print()
    
    print("All objects exist independently:")
    for i, sol in enumerate(solutions, 1):
        print(f"  Solution {i}: re_l1 = {sol.re_l1}, result = {sol.funct()}")

def show_init_vs_regular_methods():
    """Compare __init__ with regular methods"""
    print("\n\n__init__ VS REGULAR METHODS")
    print("=" * 60)
    
    print("__init__ method:")
    print("• Called automatically when object is created")
    print("• Used to set up initial state")
    print("• Takes parameters through class constructor")
    print("• Doesn't return anything visible to you")
    print()
    
    print("Regular methods (like funct):")
    print("• Called manually by you")
    print("• Use the state set up by __init__")
    print("• Can return values")
    print("• Can be called multiple times")
    print()
    
    # Demonstrate
    solution = Solution([1, 2, 3], [4, 5, 6])
    print("Example:")
    print("  solution = Solution([1,2,3], [4,5,6])  # __init__ called here")
    print(f"  result1 = solution.funct()  # Returns: {solution.funct()}")
    print(f"  result2 = solution.funct()  # Returns: {solution.funct()} (same result)")
    print("  # __init__ is never called again for the same object")

def practical_example():
    """Real-world example of using your class"""
    print("\n\nPRACTICAL EXAMPLE: DIGIT LIST CALCULATOR")
    print("=" * 60)
    
    print("Imagine you're building a system that adds numbers")
    print("represented as lists of digits (like on LeetCode):")
    print()
    
    # Sample data that might come from user input or a file
    number_pairs = [
        ([2, 4, 3], [5, 6, 4]),  # 342 + 465
        ([1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [5, 6, 4]),  # Big number
        ([9, 9, 9, 9, 9], [9, 9, 9, 9, 9]),  # 99999 + 99999
    ]
    
    total_sum = 0
    
    for i, (num1, num2) in enumerate(number_pairs, 1):
        # For each pair, create a new Solution object
        # This calls __init__ to set up the calculation
        calculator = Solution(num1, num2)
        
        # Perform the calculation
        result = calculator.funct()
        total_sum += result
        
        print(f"Calculation {i}:")
        print(f"  Input: {num1} + {num2}")
        print(f"  Result: {result}")
        print(f"  Object state: len1={calculator.len1}, len2={calculator.len2}")
        print()
    
    print(f"Total of all calculations: {total_sum}")

if __name__ == "__main__":
    demonstrate_init_step_by_step()
    test_multiple_objects()
    show_init_vs_regular_methods()
    practical_example()
    
    print("\n" + "=" * 60)
    print("KEY POINTS ABOUT YOUR __init__ METHOD:")
    print("=" * 60)
    print("✓ Automatically called when you create Solution(l1, l2)")
    print("✓ Sets up len1, len2, re_l1, re_l2 attributes")
    print("✓ Reverses the input lists for easier calculation")
    print("✓ Each object gets its own separate data")
    print("✓ Enables your funct() method to work correctly")
    print("=" * 60)
