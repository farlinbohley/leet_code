class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)
        
        # For maximum value (a): Replace the leftmost non-9 digit with 9
        max_str = num_str
        for i in range(len(num_str)):
            if num_str[i] != '9':
                max_str = num_str.replace(num_str[i], '9')
                break
        
        # For minimum value (b)
        min_str = num_str
        
        # If first digit is not 1, replace all occurrences with 1
        if num_str[0] != '1':
            min_str = num_str.replace(num_str[0], '1')
        else:
            # First digit is 1, find next digit that is not 0 or 1
            # We skip 0 because it might already be optimal
            # We skip 1 because it's the same as the first digit
            for i in range(1, len(num_str)):
                if num_str[i] != '0' and num_str[i] != '1':
                    min_str = num_str.replace(num_str[i], '0')
                    break
        
        return int(max_str) - int(min_str)


# Test with the provided examples
solution = Solution()
print(f"Example 1: num = 555")
print(f"Output: {solution.maxDiff(555)}")  # Expected: 888
print()

print(f"Example 2: num = 9")
print(f"Output: {solution.maxDiff(9)}")  # Expected: 8
print()

# Additional test cases
test_cases = [1234, 1919, 1010, 9999, 1111]
for num in test_cases:
    print(f"num = {num}, maxDiff = {solution.maxDiff(num)}")
