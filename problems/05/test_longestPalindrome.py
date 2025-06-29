from testing import Solution

def test_longest_palindrome():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("babad", ["bab", "aba"]),  # Either "bab" or "aba" is correct
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),  # Either "a" or "c" is correct
        ("racecar", ["racecar"]),
        ("noon", ["noon"]),
        ("abcdcba", ["abcdcba"]),
        ("", [""]),  # Edge case: empty string
        ("abacabad", ["abacaba"]),
        ("forgeeksskeegfor", ["geeksskeeg"]),
    ]
    
    print("Testing Longest Palindrome Solution")
    print("=" * 50)
    
    for i, (input_str, expected_outputs) in enumerate(test_cases, 1):
        result = solution.longestPalindrome(input_str)
        
        # Check if result is in the list of acceptable answers
        if result in expected_outputs:
            print(f"Test {i}: PASSED ✓")
            print(f"  Input: '{input_str}'")
            print(f"  Output: '{result}'")
        else:
            print(f"Test {i}: FAILED ✗")
            print(f"  Input: '{input_str}'")
            print(f"  Expected: {expected_outputs}")
            print(f"  Got: '{result}'")
        print()

if __name__ == "__main__":
    test_longest_palindrome() 