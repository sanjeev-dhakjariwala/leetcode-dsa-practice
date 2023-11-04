from typing import *


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(n):
            if n <= 1:
                return cost[n]
            option1 = helper(n - 1)
            option2 = helper(n - 2)
            return cost[n] + min(option1, option2)

        n = len(cost)
        
        # memoization code added
        """ memo = [-1] * (len(cost) + 1)
        def helper(i):
            if i <= 1:
                return cost[i]
            if memo[i] != -1:
                return memo[i]
            option1 = helper(i - 1)
            option2 = helper(i - 2)
            memo[i] = cost[i] + min(option1, option2)
            return memo[i] """
        option1 = helper(n - 1)
        option2 = helper(n - 2)
        return min(option1, option2)
        n = len(cost) - 1
        return min(helper(n), helper(n - 1))
"""     def minCostClimbingStairs(self, cost: List[int]) -> int:
        def helper(cost, i):
            if i >= len(cost):
                return 0
            option1 = helper(cost, i + 1)
            option2 = helper(cost, i + 2)
            return cost[i] + min(option1, option2)

        choice1 = helper(cost, 0)
        choice2 = helper(cost, 1)
        return min(choice1, choice2) """


sol = Solution()
# print(sol.minCostClimbingStairs([10, 15, 20]))
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
