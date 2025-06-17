class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        
        return False


# Test cases to verify the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Should return True
    # nums = [1, 2, 3, 4, 5] -> many triplets possible
    print(solution.increasingTriplet([1, 2, 3, 4, 5]))  # True
    
    # Test case 2: Should return False  
    # nums = [5, 4, 3, 2, 1] -> decreasing, no triplet possible
    print(solution.increasingTriplet([5, 4, 3, 2, 1]))  # False
    
    # Test case 3: Should return True
    # nums = [2, 1, 5, 0, 4, 6] -> triplet: 1 < 4 < 6 (indices 1, 4, 5)
    print(solution.increasingTriplet([2, 1, 5, 0, 4, 6]))  # True
    
    # Test case 4: Should return False
    # nums = [20, 100, 10, 12, 5, 13] -> triplet: 10 < 12 < 13 (indices 2, 3, 5)
    print(solution.increasingTriplet([20, 100, 10, 12, 5, 13]))  # True


"""
DETAILED WALKTHROUGH EXAMPLE:
nums = [2, 1, 5, 0, 4, 6]

Initial: first = ∞, second = ∞

Step 1: num = 2
- 2 <= ∞ (first), so first = 2
- State: first = 2, second = ∞

Step 2: num = 1  
- 1 <= 2 (first), so first = 1
- State: first = 1, second = ∞

Step 3: num = 5
- 5 > 1 (first) and 5 <= ∞ (second), so second = 5
- State: first = 1, second = 5
- We now have a potential pair: 1 < 5

Step 4: num = 0
- 0 <= 1 (first), so first = 0  
- State: first = 0, second = 5
- Note: We still remember we had 1 < 5, even though first changed

Step 5: num = 4
- 4 > 0 (first) and 4 <= 5 (second), so second = 4
- State: first = 0, second = 4
- We now have pair: 0 < 4 (but we also remember 1 < 5 exists)

Step 6: num = 6
- 6 > 0 (first) and 6 > 4 (second)
- We found our triplet! Even though first changed, we had a valid
  increasing pair (1 < 5) from earlier, and 6 > 5
- Return True

KEY INSIGHT: The algorithm maintains the smallest possible values for 
first and second positions, which gives us the best chance of finding 
a third element. Even if 'first' gets updated, we don't lose track of 
previously found valid pairs.
""" 