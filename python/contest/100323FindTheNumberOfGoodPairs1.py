from typing import *

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        c = 0
        for i in range(n1):
            for j in range(n2):
                if nums1[i] % (nums2[j] * k) == 0:
                    c += 1
        return c

sol = Solution()
nums1 = [1, 3, 4]
nums2 = [1, 3, 4]
print(sol.numberOfPairs(nums1, nums2, 1))