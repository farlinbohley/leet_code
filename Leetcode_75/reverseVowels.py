class Solution:
    
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vow_list = []
        for i, char in enumerate(s):
            if char in vowels:
                vow_list.append(char)
        
        re_vow_list = list(reversed(vow_list))  # Convert iterator to list
        s = list(s)  # Convert string to list for modification
        
        vow_index = 0  # Track position in reversed vowel list
        for i, char in enumerate(s):
            if char in vowels:
                s[i] = re_vow_list[vow_index]
                vow_index += 1
        
        return ''.join(s)  # Convert back to string