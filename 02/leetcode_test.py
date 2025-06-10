#!/usr/bin/env python3
"""
LeetCode-style test for Add Two Numbers
This mimics exactly how LeetCode would test your solution
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """LeetCode entry point - converts ListNode to lists, uses your algorithm, converts back"""
        # Convert ListNodes to regular lists
        list1 = self._listnode_to_list(l1)
        list2 = self._listnode_to_list(l2)
        
        # Use your excellent algorithm
        result_list = self._your_algorithm(list1, list2)
        
        # Convert result back to ListNode
        return self._list_to_listnode(result_list)
    
    def _listnode_to_list(self, head: ListNode) -> list[int]:
        """Convert ListNode to Python list"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def _list_to_listnode(self, lst: list[int]) -> ListNode:
        """Convert Python list back to ListNode"""
        if not lst:
            return ListNode(0)
        
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def _your_algorithm(self, l1: list[int], l2: list[int]) -> list[int]:
        """Your original algorithm, slightly modified"""
        self.len1 = len(l1)
        self.len2 = len(l2)
        self.re_l1 = {}
        self.re_l2 = {}
        for i in range(len(l1)):
            self.re_l1[i] = l1[self.len1 - 1 - i]
        for i in range(len(l2)):
            self.re_l2[i] = l2[self.len2 - 1 - i]
        num_1 = 0
        num_2 = 0
        for i in range(len(self.re_l1)):
            num_1 = num_1 + (10 ** i)*self.re_l1[i]
        for i in range(len(self.re_l2)):
            num_2 = num_2 + (10 ** i)*self.re_l2[i]
        self.grand_total = num_2 + num_1
        
        if self.grand_total == 0:
            return [0]

        # Convert the number to a string
        s_grand_total = str(self.grand_total)
        
        answer = []
        # Iterate through the characters of the string and convert them back to int
        for digit_char in s_grand_total:
            answer.append(int(digit_char))
            
        # Reverse the answer since LeetCode expects digits in reverse order
        return answer[::-1]

# Test exactly like LeetCode would
def main():
    # This is exactly how LeetCode calls your code
    solution = Solution()
    
    # Test case: [2,4,3] + [5,6,4] = [7,0,8]
    # Create ListNodes
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    # Call your method (this is what LeetCode does)
    result = solution.addTwoNumbers(l1, l2)
    
    # Print result
    print("LeetCode-style test result:")
    current = result
    output = []
    while current:
        output.append(str(current.val))
        current = current.next
    
    print(f"Output: [{','.join(output)}]")
    print("Expected: [7,0,8]")
    print(f"Success: {output == ['7','0','8']}")

if __name__ == "__main__":
    main()
