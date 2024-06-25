from typing import *


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        print(nums)
        n = len(nums)
        i = 0
        j = n - 1
        res = []
        while i < j:
            temp = (nums[i] + nums[j]) / 2
            res.append(temp)
            i += 1
            j -= 1
        print(res)
        res.sort()
        return res[0]


sol = Solution()
nums = [7, 8, 3, 4, 15, 13, 4, 1]
print(sol.minimumAverage(nums))
