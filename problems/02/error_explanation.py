"""
EXPLANATION: Why you got the TypeError and how to fix it

ERROR MESSAGE:
TypeError: Solution.__init__() missing 2 required positional arguments: 'l1' and 'l2'

PROBLEM:
========
Your original code:
    class Solution:
        def __init__(self, l1: list[int], l2: list[int]):  # ❌ Takes parameters
            # ... setup code ...

LeetCode's testing system does:
    solution = Solution()  # ❌ No arguments provided!
    result = solution.addTwoNumbers(param_1, param_2)

This causes the error because LeetCode expects:
- Solution() with NO arguments
- Then call methods WITH arguments

SOLUTION:
=========
Change your class structure to match LeetCode's expectations:

✅ CORRECT LeetCode Format:
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):  # ✅ No parameters!
        # Any initialization code goes here
        pass
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:  # ✅ Parameters go here!
        # Your algorithm goes here
        # Process l1 and l2 to create result
        pass

"""
KEY DIFFERENCES:

❌ YOUR ORIGINAL APPROACH:
   solution = Solution(l1, l2)        # Pass data to constructor
   result = solution.funct()          # Call method with no parameters

✅ LEETCODE EXPECTED APPROACH:
   solution = Solution()              # Create object with no parameters
   result = solution.addTwoNumbers(l1, l2)  # Pass data to method

WHY LEETCODE DOES IT THIS WAY:
==============================
1. REUSABILITY: One Solution object can handle multiple test cases
2. STANDARDIZATION: All LeetCode problems follow this pattern
3. EFFICIENCY: Don't recreate objects for each test case

EXAMPLE USAGE:
==============
"""

def demonstrate_correct_usage():
    # This is how LeetCode's testing system works:
    solution = Solution()  # Create once, no arguments
    
    # Test case 1
    l1_case1 = ListNode(2)  # Create linked list for test 1
    l2_case1 = ListNode(5)
    result1 = solution.addTwoNumbers(l1_case1, l2_case1)
    
    # Test case 2 - same solution object, different inputs
    l1_case2 = ListNode(9)  # Create linked list for test 2  
    l2_case2 = ListNode(1)
    result2 = solution.addTwoNumbers(l1_case2, l2_case2)
    
    # Test case 3 - same solution object again
    l1_case3 = ListNode(0)
    l2_case3 = ListNode(0)
    result3 = solution.addTwoNumbers(l1_case3, l2_case3)
    
    print("All tests use the SAME Solution object!")
    print("But each method call gets DIFFERENT parameters!")

"""
HOW TO ADAPT YOUR ALGORITHM:
============================
1. Move your __init__ parameters to the method
2. Make __init__ parameter-free
3. Process inputs inside the method instead of storing them

Your original algorithm concept was good, just needed restructuring!
"""

if __name__ == "__main__":
    print(__doc__)
    demonstrate_correct_usage()
