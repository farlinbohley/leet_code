class Solution:
    def compress(self, chars):
        """
        443. String Compression
        Compress array of characters in-place using consecutive character groups.
        """
        write_pos = 0  # Position to write compressed data
        i = 0          # Position to read from
        
        while i < len(chars):
            current_char = chars[i]
            count = 1
            
            # Count consecutive occurrences
            while i + count < len(chars) and chars[i + count] == current_char:
                count += 1
            
            # Write the character
            chars[write_pos] = current_char
            write_pos += 1
            
            # Write the count if > 1
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write_pos] = digit
                    write_pos += 1
            
            # Move to next group
            i += count
        
        return write_pos

def main():
    solution = Solution()
    
    # Test case 1: ["a","a","b","b","c","c","c"] -> ["a","2","b","2","c","3"]
    test1 = ["a", "a", "b", "b", "c", "c", "c"]
    original1 = test1.copy()
    
    print("Test 1 - Original:", original1)
    result1 = solution.compress(test1)
    print("Test 1 - Compressed:", test1[:result1], "| Length:", result1)
    
    # Test case 2: ["a"] -> ["a"]
    test2 = ["a"]
    original2 = test2.copy()
    
    print("\nTest 2 - Original:", original2)
    result2 = solution.compress(test2)
    print("Test 2 - Compressed:", test2[:result2], "| Length:", result2)
    
    # Test case 3: ["a","b","b","b","b","b","b","b","b","b","b","b","b"] -> ["a","b","1","2"]
    test3 = ["a"] + ["b"] * 12
    original3 = test3.copy()
    
    print("\nTest 3 - Original:", original3)
    result3 = solution.compress(test3)
    print("Test 3 - Compressed:", test3[:result3], "| Length:", result3)
    
    # Additional test case: Edge case with larger numbers
    test4 = ["a"] * 100
    original4_preview = str(test4[:5])[:-1] + ", ... (100 'a's total)]"
    
    print(f"\nTest 4 - Original: {original4_preview}")
    result4 = solution.compress(test4)
    print("Test 4 - Compressed:", test4[:result4], "| Length:", result4)

if __name__ == "__main__":
    main()

