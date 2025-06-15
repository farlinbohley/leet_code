class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        most_candies = max(candies)
        check = []
        for i, can in enumerate(candies):
            if (can + extraCandies) < most_candies:
                check.append(False)
            else:
                check.append(True)
        return check
