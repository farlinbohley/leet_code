class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start = 0
        max_len = 0
        
        def expand_around_center(left: int, right: int) -> int:
            """Helper function to expand around a center and return the length of palindrome."""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome
            return right - left - 1
        
        for i in range(len(s)):
            # Check for odd-length palindromes (center is a single character)
            len1 = expand_around_center(i, i)
            # Check for even-length palindromes (center is between two characters)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length from both cases
            current_len = max(len1, len2)
            
            # Update the result if we found a longer palindrome
            if current_len > max_len:
                max_len = current_len
                # Calculate the starting position of the palindrome
                start = i - (current_len - 1) // 2
        
        return s[start:start + max_len]
    
    def longestPalindromeLength(self, s: str) -> int:
        """Helper method to just return the length of the longest palindrome."""
        return len(self.longestPalindrome(s))

if __name__ == '__main__':
    # Create an instance of the Solution class
    solver = Solution()

    # Define test cases
    test_strings = ["babad", "cbbd", "a", "ac", "racecar", "noon", "abcdef", ""]

    # Run test cases
    for test_str in test_strings:
        print(f"Input string: '{test_str}'")
        longest_p = solver.longestPalindrome(test_str)
        print(f"Longest palindromic substring: '{longest_p}'")
        print(f"Length: {len(longest_p)}")
        print("-" * 30)
            
