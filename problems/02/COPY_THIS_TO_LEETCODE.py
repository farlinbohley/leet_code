class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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
        """Your algorithm - fixed to handle LeetCode's digit order correctly"""
        # Convert list to number (digits are already in reverse order)
        num_1 = 0
        for i, digit in enumerate(l1):
            num_1 += digit * (10 ** i)
            
        num_2 = 0
        for i, digit in enumerate(l2):
            num_2 += digit * (10 ** i)
        
        total = num_1 + num_2
        
        if total == 0:
            return [0]

        # Convert result back to digit list (in reverse order)
        result = []
        while total > 0:
            result.append(total % 10)
            total //= 10
            
        return result
