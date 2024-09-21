from typing import *


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        fix = 0
        moving = 1

        n = len(nums)
        c = 1
        
        while moving < n - 2:
            if nums[fix] != nums[moving]:
                k -= 1
            else:
                c += 1
            moving += 1

        return (moving - fix) + 1


sol = Solution()
nums = [1, 2, 3, 4, 5, 1]
k = 0
print(sol.maximumLength(nums, k))
