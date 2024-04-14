from typing import *


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res1 = []
        res2 = []
        res1.append(nums[0])
        for i in range(1, n):
            if len(res2) >= 1 and res1[-1] > res2[-1]:
                res1.append(nums[i])
            else:
                res2.append(nums[i])
        return res1 + res2


sol = Solution()
print(sol.resultArray([5, 4, 3, 8]))
