# Your approach adapted to work with LeetCode format
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        # LeetCode expects __init__ with NO parameters
        pass
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Convert linked lists to Python lists
        list1 = self._linked_list_to_list(l1)
        list2 = self._linked_list_to_list(l2)
        
        # Use your algorithm to get the sum
        sum_result = self._add_reversed_lists(list1, list2)
        
        # Convert the sum back to a linked list
        return self._number_to_linked_list(sum_result)
    
    def _linked_list_to_list(self, head: ListNode) -> List[int]:
        """Convert linked list to Python list"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def _add_reversed_lists(self, l1: List[int], l2: List[int]) -> int:
        """Your original algorithm adapted"""
        # Reverse the lists and convert to numbers
        num1 = 0
        for i in range(len(l1)):
            num1 += l1[i] * (10 ** i)
        
        num2 = 0
        for i in range(len(l2)):
            num2 += l2[i] * (10 ** i)
        
        return num1 + num2
    
    def _number_to_linked_list(self, num: int) -> ListNode:
        """Convert a number back to linked list in reverse order"""
        if num == 0:
            return ListNode(0)
        
        dummy_head = ListNode(0)
        current = dummy_head
        
        while num > 0:
            digit = num % 10
            current.next = ListNode(digit)
            current = current.next
            num //= 10
        
        return dummy_head.next

# Helper functions for testing
def list_to_linked_list(arr):
    """Convert a Python list to a linked list"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert a linked list to a Python list"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test the solution
if __name__ == "__main__":
    solution = Solution()  # ✅ No arguments - this is what LeetCode expects!
    
    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    l1 = list_to_linked_list([2, 4, 3])  # represents 342
    l2 = list_to_linked_list([5, 6, 4])  # represents 465
    result = solution.addTwoNumbers(l1, l2)  # ✅ Pass parameters to the method
    result_list = linked_list_to_list(result)
    print(f"Your algorithm: [2,4,3] + [5,6,4] = {result_list}")
    
    # Test case 2: [0] + [0] = [0]
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(f"Your algorithm: [0] + [0] = {result_list}")
    
    print("\n" + "="*50)
    print("KEY DIFFERENCES FROM YOUR ORIGINAL:")
    print("="*50)
    print("❌ OLD: def __init__(self, l1: list[int], l2: list[int])")
    print("✅ NEW: def __init__(self):")
    print("")
    print("❌ OLD: solution = Solution(l1, l2)")
    print("✅ NEW: solution = Solution()")
    print("        result = solution.addTwoNumbers(l1, l2)")
    print("")
    print("LeetCode creates Solution() once, then calls methods with different inputs!")
    print("="*50)
