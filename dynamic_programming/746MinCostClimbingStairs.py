from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n):
            if n <= 1:
                return cost[n]
            return cost[n] + min(helper(n - 1), helper(n - 2))

        n = len(cost)
        return min(helper(n - 1), helper(n - 2))


sol = Solution()
print(sol.minCostClimbingStairs([10, 15, 20]))
