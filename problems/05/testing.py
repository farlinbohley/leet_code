class Solution:
    def longestPalindrome(self, s: str) -> str:
        def Expan(l, r):
            '''Expand around center and return the length of palindrome'''
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Return the length of the palindrome
            return (r - l - 1)
        
        max_len = 0
        start = 0
        
        for i in range(len(s)):
            # Check for odd-length palindromes (single center)
            len1 = Expan(i, i)
            # Check for even-length palindromes (two centers)
            len2 = Expan(i, i + 1)
            
            # Get the maximum length from both cases
            cur_len = max(len1, len2)
            
            # If we found a longer palindrome, update our records
            if cur_len > max_len:
                max_len = cur_len
                # Calculate the starting position
                # For odd palindromes: i is the center
                # For even palindromes: i and i+1 are the two centers
                start = i - (cur_len - 1) // 2
        
        # Simply slice the string to get the palindrome
        return s[start:start + max_len]
