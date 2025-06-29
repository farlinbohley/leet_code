class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        min_len = min(len(word1), len(word2))
        
        # Alternate characters for the common length
        for i in range(min_len):
            result.append(word1[i])
            result.append(word2[i])
        
        # Append remaining characters (only one of these will have content)
        result.append(word1[min_len:])
        result.append(word2[min_len:])
        
        return "".join(result)

# Alternative even more optimized approach using itertools
from itertools import zip_longest

class SolutionOptimal:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for c1, c2 in zip_longest(word1, word2, fillvalue=''):
            if c1:
                result.append(c1)
            if c2:
                result.append(c2)
        return "".join(result)
