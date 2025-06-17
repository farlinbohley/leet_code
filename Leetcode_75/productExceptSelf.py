class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        total = 1
        zeros = 0
        product = []
        for i in range(len(nums)):
            if nums[i] != 0:
                total = total * nums[i]
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
        if zeros >= 2:
            product = [0] * len(nums)
        elif zeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    product.append(int(total))
                else:
                    product.append(0)
        else:
            for i in range(len(nums)):
                product.append(int(total // nums[i]))
        return product

# Test program
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 2, 3, 4]
    result1 = solution.productExceptSelf(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")
    print(f"Expected: [24, 12, 8, 6]")
    print()
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    result2 = solution.productExceptSelf(nums2)
    print(f"Input: {nums2}")
    print(f"Output: {result2}")
    print(f"Expected: [0, 0, 9, 0, 0]")
    print()
    
    # Test case 3
    nums3 = [2, 3, 4]
    result3 = solution.productExceptSelf(nums3)
    print(f"Input: {nums3}")
    print(f"Output: {result3}")
    print(f"Expected: [12, 8, 6]")
