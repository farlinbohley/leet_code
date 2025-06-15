class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        
        # We add a 0 at the beginning and end of the flowerbed
        # to handle edge cases for the first and last plots.
        f = [0] + flowerbed + [0]
        
        count = 0
        for i in range(1, len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1  # Plant a flower here
                count += 1
        
        return count >= n