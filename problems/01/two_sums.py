from typing import List

class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_to_index = {}  # Initialize an empty dictionary here
      for index in range(len(nums)):
         num = nums[index]
         complement = target - num
         if complement in num_to_index:
            # If the complement is already in our dictionary, we found a pair!
            return [num_to_index[complement], index]
         # If not, store the current number and its index
         num_to_index[num] = index
      return []  # Return an empty list if no solution is found




