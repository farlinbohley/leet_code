
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        chars = []
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            chars.append(word1[i])
            chars.append(word2[i])

        chars.append(word1[min_len:])
        chars.append(word2[min_len:])
        return "".join(chars)
