# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy head to simplify the logic
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Process both linked lists
        while l1 or l2 or carry:
            # Get values from current nodes (or 0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
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
    solution = Solution()  # No arguments needed!
    
    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    l1 = list_to_linked_list([2, 4, 3])  # represents 342
    l2 = list_to_linked_list([5, 6, 4])  # represents 465
    result = solution.addTwoNumbers(l1, l2)  # Call method with parameters
    result_list = linked_list_to_list(result)
    print(f"Test 1: [2,4,3] + [5,6,4] = {result_list}")  # Should be [7,0,8] (represents 807)
    
    # Test case 2: [0] + [0] = [0]
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(f"Test 2: [0] + [0] = {result_list}")
    
    # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = solution.addTwoNumbers(l1, l2)
    result_list = linked_list_to_list(result)
    print(f"Test 3: [9,9,9,9,9,9,9] + [9,9,9,9] = {result_list}")
