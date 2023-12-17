from typing import *


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        while i < n:
            if i + k < n:
                if nums[i + k] - nums[i] <= k:
                    res.append(nums[i : (i + k + 1)])
                    i += k
            i += k

        return res


sol = Solution()
print(sol.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
print(sol.divideArray([1, 3, 3, 2, 7, 3], 3))
print(sol.divideArray([1,3,4,8,7,9,3,5,1], 2))
print(sol.divideArray([4, 2, 9, 8, 2, 12, 7, 12, 10, 5, 8, 5, 5, 7, 9, 2, 5, 11], 14))
