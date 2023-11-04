from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(i):
            if i <= 1:
                return nums[i]
            option1 = nums[i] + helper(i - 2)
            option2 = helper(i - 1)
            return max(option1, option2)

        n = len(nums)
        option1 = helper(n - 1)
        return option1
sol = Solution()
print(sol.rob([2,1]))
