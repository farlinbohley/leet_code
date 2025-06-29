#!/usr/bin/env python3
"""
Simple test for add_two_numbers.py
"""

from add_two_numbers import Solution

# Test Case 1: [2,4,3] + [5,6,4] should equal 342 + 465 = 807
print("Test Case 1:")
l1 = [2, 4, 3]  # represents 342
l2 = [5, 6, 4]  # represents 465
print(f"List 1: {l1}")
print(f"List 2: {l2}")

# This calls __init__ automatically
solution = Solution(l1, l2)

# Check what __init__ created
print(f"After __init__:")
print(f"  len1 = {solution.len1}")
print(f"  len2 = {solution.len2}")
print(f"  re_l1 = {solution.re_l1}")
print(f"  re_l2 = {solution.re_l2}")

# Get the result
result = solution.funct()
print(f"Result: {result}")
print(f"Expected: 807")
print(f"Test {'PASSED' if result == 807 else 'FAILED'}")

print("\n" + "="*40)
print("How __init__ works:")
print("1. You call: Solution(l1, l2)")
print("2. Python automatically calls __init__(self, l1, l2)")
print("3. __init__ sets up the object's attributes")
print("4. You can then call methods on the object")
print("="*40)
