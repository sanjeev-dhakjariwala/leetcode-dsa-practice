from typing import *


class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}

        def helperMemo(i, rem):
            if (i, n) in dp:
                return dp[(i, n)]
            if i == n - 1 and rem == 0:
                return True
            if i >= n or rem < 0:
                return False

            include = helperMemo(i + 1, rem - nums[i])
            exclude = helperMemo(i + 1, rem)
            dp[(i, rem)] = include or exclude
            return include or exclude

        def helper1DDP():
            total_sum = sum(nums)
            if total_sum % 2 != 0:
                return False

            target_sum = total_sum // 2
            dp = [False] * (target_sum + 1)
            dp[0] = True

            for num in nums:
                for j in range(target_sum, num - 1, -1):
                    dp[j] = dp[j] or dp[j - num]

            return dp[target_sum]
        return helper1DDP()


sol = Solution()
print(sol.canPartition([1, 5, 11, 5]))
