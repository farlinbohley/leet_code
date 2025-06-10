#!/usr/bin/env python3
"""
Test file for add_two_numbers.py
Demonstrates how to use the Solution class with __init__ method
"""

from add_two_numbers import Solution

def test_add_two_numbers():
    """Test the Solution class with various test cases"""
    
    print("Testing Add Two Numbers Program")
    print("=" * 40)
    
    # Test Case 1: [2,4,3] + [5,6,4] = 342 + 465 = 807
    print("\nTest Case 1:")
    l1 = [2, 4, 3]  # represents 342
    l2 = [5, 6, 4]  # represents 465
    print(f"List 1: {l1} (represents number: 342)")
    print(f"List 2: {l2} (represents number: 465)")
    print(f"Expected sum: 342 + 465 = 807")
    
    # Create Solution instance with the two lists
    solution1 = Solution(l1, l2)
    result1 = solution1.funct()
    print(f"Actual result: {result1}")
    print(f"Test 1 {'PASSED' if result1 == 807 else 'FAILED'}")
    
    # Test Case 2: [0] + [0] = 0 + 0 = 0
    print("\nTest Case 2:")
    l1 = [0]
    l2 = [0]
    print(f"List 1: {l1} (represents number: 0)")
    print(f"List 2: {l2} (represents number: 0)")
    print(f"Expected sum: 0 + 0 = 0")
    
    solution2 = Solution(l1, l2)
    result2 = solution2.funct()
    print(f"Actual result: {result2}")
    print(f"Test 2 {'PASSED' if result2 == 0 else 'FAILED'}")
    
    # Test Case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = 9999999 + 9999 = 10009998
    print("\nTest Case 3:")
    l1 = [9, 9, 9, 9, 9, 9, 9]  # represents 9999999
    l2 = [9, 9, 9, 9]           # represents 9999
    print(f"List 1: {l1} (represents number: 9999999)")
    print(f"List 2: {l2} (represents number: 9999)")
    print(f"Expected sum: 9999999 + 9999 = 10009998")
    
    solution3 = Solution(l1, l2)
    result3 = solution3.funct()
    print(f"Actual result: {result3}")
    print(f"Test 3 {'PASSED' if result3 == 10009998 else 'FAILED'}")
    
    # Test Case 4: Single digit numbers
    print("\nTest Case 4:")
    l1 = [5]  # represents 5
    l2 = [7]  # represents 7
    print(f"List 1: {l1} (represents number: 5)")
    print(f"List 2: {l2} (represents number: 7)")
    print(f"Expected sum: 5 + 7 = 12")
    
    solution4 = Solution(l1, l2)
    result4 = solution4.funct()
    print(f"Actual result: {result4}")
    print(f"Test 4 {'PASSED' if result4 == 12 else 'FAILED'}")
    
    # Test Case 5: Different lengths
    print("\nTest Case 5:")
    l1 = [1, 2]     # represents 21
    l2 = [9, 9, 9]  # represents 999
    print(f"List 1: {l1} (represents number: 21)")
    print(f"List 2: {l2} (represents number: 999)")
    print(f"Expected sum: 21 + 999 = 1020")
    
    solution5 = Solution(l1, l2)
    result5 = solution5.funct()
    print(f"Actual result: {result5}")
    print(f"Test 5 {'PASSED' if result5 == 1020 else 'FAILED'}")

def demonstrate_init_usage():
    """Demonstrate how __init__ works step by step"""
    
    print("\n" + "=" * 50)
    print("Demonstrating __init__ method usage:")
    print("=" * 50)
    
    # Show what happens when we create an instance
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    
    print(f"\nCreating Solution instance with:")
    print(f"l1 = {l1}")
    print(f"l2 = {l2}")
    print("\nCalling: solution = Solution(l1, l2)")
    
    # Create the instance (this calls __init__)
    solution = Solution(l1, l2)
    
    print("\nAfter __init__ is called, the instance has:")
    print(f"solution.len1 = {solution.len1}")
    print(f"solution.len2 = {solution.len2}")
    print(f"solution.re_l1 = {solution.re_l1}")
    print(f"solution.re_l2 = {solution.re_l2}")
    
    print(f"\nCalling solution.funct() returns: {solution.funct()}")

def show_how_conversion_works():
    """Show how the list-to-number conversion works"""
    
    print("\n" + "=" * 50)
    print("How the list-to-number conversion works:")
    print("=" * 50)
    
    l1 = [2, 4, 3]  # This should represent 342
    
    print(f"\nOriginal list: {l1}")
    print("Your algorithm reverses the list and converts to number:")
    
    # Simulate what your __init__ does
    len1 = len(l1)
    re_l1 = {}
    
    print(f"\nStep 1: Reverse the list")
    for i in range(len(l1)):
        re_l1[i] = l1[len1 - 1 - i]  # Fixed the indexing
        print(f"  re_l1[{i}] = l1[{len1 - 1 - i}] = {l1[len1 - 1 - i]}")
    
    print(f"\nReversed dictionary: {re_l1}")
    
    print(f"\nStep 2: Convert to number using powers of 10:")
    num = 0
    for i in range(len(re_l1)):
        contribution = (10 ** i) * re_l1[i]
        num += contribution
        print(f"  Position {i}: {re_l1[i]} × 10^{i} = {re_l1[i]} × {10**i} = {contribution}")
    
    print(f"\nFinal number: {num}")

if __name__ == "__main__":
    # Run all tests
    test_add_two_numbers()
    demonstrate_init_usage()
    show_how_conversion_works()
    
    print("\n" + "=" * 50)
    print("Test Summary:")
    print("This demonstrates how your __init__ method works in practice.")
    print("Each test case creates a new Solution instance, which calls __init__")
    print("automatically to set up the object's state.")
    print("=" * 50)
