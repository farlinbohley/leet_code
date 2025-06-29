from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Double loop approach - more intuitive but less efficient O(n²)
        
        # Outer loop: iterate through each number
        for i in range(len(nums)):
            # Inner loop: check all numbers that come after the current number
            for j in range(i + 1, len(nums)):
                # Check if the sum of these two numbers equals the target
                if nums[i] + nums[j] == target:
                    return [i, j]  # Found the pair, return their indices
        
        # No solution found
        return []

# Example usage and testing
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    print(f"Test 1 - nums: {nums1}, target: {target1}")
    print(f"Result: {result1}")
    print(f"Verification: nums[{result1[0]}] + nums[{result1[1]}] = {nums1[result1[0]]} + {nums1[result1[1]]} = {nums1[result1[0]] + nums1[result1[1]]}")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    print(f"Test 2 - nums: {nums2}, target: {target2}")
    print(f"Result: {result2}")
    print(f"Verification: nums[{result2[0]}] + nums[{result2[1]}] = {nums2[result2[0]]} + {nums2[result2[1]]} = {nums2[result2[0]] + nums2[result2[1]]}")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    print(f"Test 3 - nums: {nums3}, target: {target3}")
    print(f"Result: {result3}")
    print(f"Verification: nums[{result3[0]}] + nums[{result3[1]}] = {nums3[result3[0]]} + {nums3[result3[1]]} = {nums3[result3[0]] + nums3[result3[1]]}")
    print()
    
    # Test case 4 - No solution
    nums4 = [1, 2, 3]
    target4 = 7
    result4 = solution.twoSum(nums4, target4)
    print(f"Test 4 - nums: {nums4}, target: {target4}")
    if result4:
        print(f"Result: {result4}")
    else:
        print("Result: No solution found")
