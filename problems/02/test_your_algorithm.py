#!/usr/bin/env python3
"""
Test your modified add_two_numbers algorithm
"""

from add_two_numbers import Solution, ListNode

def create_linked_list(arr):
    """Helper to create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Helper to convert linked list back to array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_your_algorithm():
    solution = Solution()
    
    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    # Represents: 342 + 465 = 807
    print("Test Case 1:")
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    result_array = linked_list_to_array(result)
    print(f"Input: [2,4,3] + [5,6,4]")
    print(f"Output: {result_array}")
    print(f"Expected: [7,0,8]")
    print(f"Test 1: {'PASSED' if result_array == [7,0,8] else 'FAILED'}")
    
    # Test case 2: [0] + [0] = [0]
    print("\nTest Case 2:")
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    result_array = linked_list_to_array(result)
    print(f"Input: [0] + [0]")
    print(f"Output: {result_array}")
    print(f"Expected: [0]")
    print(f"Test 2: {'PASSED' if result_array == [0] else 'FAILED'}")
    
    # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    print("\nTest Case 3:")
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    result = solution.addTwoNumbers(l1, l2)
    result_array = linked_list_to_array(result)
    print(f"Input: [9,9,9,9,9,9,9] + [9,9,9,9]")
    print(f"Output: {result_array}")
    print(f"Expected: [8,9,9,9,0,0,0,1]")
    print(f"Test 3: {'PASSED' if result_array == [8,9,9,9,0,0,0,1] else 'FAILED'}")

if __name__ == "__main__":
    test_your_algorithm()
