class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Merge the two arrays
        merged = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
           
        # Add ALL remaining elements from nums1
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        
        # Add ALL remaining elements from nums2  
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        if self.checkOdd(merged):
            return merged[len(merged) // 2 ]
        else:
            mid = len(merged) // 2
            return (merged[mid - 1] + merged[mid]) / 2 

    def checkOdd(self, ls) -> bool:
        if len(ls) % 2 == 1:
            return True
        return False


def test():
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3, 6, 10], [2, 5, 8, 11]))
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))

if __name__ == "__main__":
    test()