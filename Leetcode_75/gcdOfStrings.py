
class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd_length = self.gcd(len(str1), len(str2))
        return str1[:gcd_length]
