from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def helperMemo(i):
            if i in dp:
                return dp[i]
            if i >= len(cost):
                return 0
            cost1 = helperMemo(i + 1)
            cost2 = helperMemo(i + 2)
            dp[i] = cost[i] + min(cost1, cost2)
            return cost[i] + min(cost1, cost2)

        dp = {}
        # return min(helperMemo(0), helperMemo(1))

        def helper(i):
            if i == (len(cost) - 1):
                return cost[i]
            if i >= len(cost):
                return 0
            cost1 = helper(i + 1)
            cost2 = helper(i + 2)
            finalCost = cost[i] + min(cost1, cost2)
            return finalCost

        return min(helper(0), helper(1))


sol = Solution()
# print(sol.minCostClimbingStairs([10, 15, 20]))
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
