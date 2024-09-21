from typing import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        num_sum = sum(nums)
        return expected - num_sum


sol = Solution()
print(sol.missingNumber([3, 0, 1]))
