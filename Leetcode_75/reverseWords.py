class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        words = {}
        word_count = 0
        pro_string = ""
        for i in range(len(s)):
            if s[i] == " ":
                words[word_count] = s[start: i]
                start = i + 1
                word_count += 1
        # Add the last word (which doesn't end with a space)
        words[word_count] = s[start:]
        word_count += 1
        for i in range(word_count):
            pro_string += words[word_count - i - 1] + " "
        
        # Remove the trailing space
        pro_string = pro_string.strip()
        
        # Remove multiple spaces using replace()
        while "  " in pro_string:
            pro_string = pro_string.replace("  ", " ")
            
        return pro_string

# Test program
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases from the problem
    test_cases = [
        "the sky is blue",
        "  hello world  ", 
        "a good   example"
    ]
    
    expected_outputs = [
        "blue is sky the",
        "world hello",
        "example good a"
    ]
    
    print("Testing reverseWords function:")
    print("-" * 40)
    
    for i, test_input in enumerate(test_cases):
        result = solution.reverseWords(test_input)
        expected = expected_outputs[i]
        
        print(f"Test {i+1}:")
        print(f"Input: '{test_input}'")
        print(f"Expected: '{expected}'")
        print(f"Got: '{result}'")
        print(f"Passed: {result == expected}")
        print("-" * 40)