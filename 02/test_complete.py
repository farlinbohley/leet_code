#!/usr/bin/env python3
"""
Complete test of Add Two Numbers algorithm
Tests both the original algorithm and LeetCode wrapper
"""

from add_two_numbers import Solution, ListNode

def create_listnode(digits):
    """Helper to create ListNode from list of digits"""
    if not digits:
        return ListNode(0)
    
    head = ListNode(digits[0])
    current = head
    for digit in digits[1:]:
        current.next = ListNode(digit)
        current = current.next
    return head

def listnode_to_list(head):
    """Helper to convert ListNode back to list for display"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_algorithm():
    """Test the complete algorithm"""
    solution = Solution()
    
    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    print("Test case 1: [2,4,3] + [5,6,4] = [7,0,8]")
    l1 = create_listnode([2, 4, 3])  # represents 342
    l2 = create_listnode([5, 6, 4])  # represents 465
    result = solution.addTwoNumbers(l1, l2)
    result_list = listnode_to_list(result)
    print(f"Result: {result_list}")
    print(f"Expected: [7, 0, 8]")
    print(f"Correct: {result_list == [7, 0, 8]}")
    print()
    
    # Test case 2: [0] + [0] = [0]
    print("Test case 2: [0] + [0] = [0]")
    l1 = create_listnode([0])
    l2 = create_listnode([0])
    result = solution.addTwoNumbers(l1, l2)
    result_list = listnode_to_list(result)
    print(f"Result: {result_list}")
    print(f"Expected: [0]")
    print(f"Correct: {result_list == [0]}")
    print()
    
    # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    print("Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]")
    l1 = create_listnode([9,9,9,9,9,9,9])  # represents 9999999
    l2 = create_listnode([9,9,9,9])        # represents 9999  
    result = solution.addTwoNumbers(l1, l2)
    result_list = listnode_to_list(result)
    print(f"Result: {result_list}")
    print(f"Expected: [8,9,9,9,0,0,0,1]")
    print(f"Correct: {result_list == [8,9,9,9,0,0,0,1]}")
    print()
    
    # Test your original algorithm directly
    print("Testing your original algorithm directly:")
    print("Direct algorithm test: [2,4,3] + [5,6,4]")
    direct_result = solution._your_algorithm([2,4,3], [5,6,4])
    print(f"Direct result: {direct_result}")
    print(f"Expected: [7, 0, 8]")
    print(f"Correct: {direct_result == [7, 0, 8]}")

if __name__ == "__main__":
    test_algorithm()
