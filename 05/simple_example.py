# Simple example of expand around centers algorithm

def expand_from_center(s, left, right):
    """
    Expand from the center and return the length of the palindrome
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        print(f"  Comparing s[{left}]='{s[left]}' with s[{right}]='{s[right]}' - Match!")
        left -= 1
        right += 1
    
    print(f"  Stopped at left={left}, right={right}")
    return right - left - 1

# Example: Finding palindromes in "babad"
s = "babad"
print(f"String: '{s}'")
print("=" * 40)

for i in range(len(s)):
    print(f"\nCenter at index {i} ('{s[i]}')")
    
    # Check odd length palindrome
    print("  Checking odd length:")
    odd_length = expand_from_center(s, i, i)
    print(f"  Odd palindrome length: {odd_length}")
    
    # Check even length palindrome
    if i < len(s) - 1:
        print("  Checking even length:")
        even_length = expand_from_center(s, i, i + 1)
        print(f"  Even palindrome length: {even_length}")

# Show how to extract the palindrome substring
print("\n" + "=" * 40)
print("Example: Extracting palindrome at center index 2:")
center = 2
length = 3  # We found a palindrome of length 3
start = center - (length - 1) // 2
end = start + length
print(f"Palindrome: '{s[start:end]}'")  # Output: 'bab' 