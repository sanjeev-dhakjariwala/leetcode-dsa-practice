from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def helper(i):
            if i in dp:
                return dp[i]
            if i >= n:
                return 0
            ans1 = nums[i] + helper(i + 2)
            ans2 = helper(i + 1)
            dp[i] = max(ans1, ans2)
            return dp[i]
        
        return helper(0)


sol = Solution()
print(sol.rob([2, 7, 9, 3, 1]))
