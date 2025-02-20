from typing import *


class Solution:

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     memo = {}
    #
    #     def dfs(prev, next, depth):
    #         if next == len(nums):
    #             return 0
    #         include = 0
    #         if prev == -1 or nums[next] > nums[prev]:
    #             include = 1 + dfs(next, next + 1, depth + 1)
    #         exclude = dfs(prev, next + 1, depth + 1)
    #         res = max(include, exclude)
    #         memo[(prev, next)] = res
    #
    #         # Print the recursion tree
    #         print("  " * depth, f"dfs({prev}, {next}), include: {include}, exclude: {exclude}, result: {res}")
    #
    #         return res

    # return dfs(-1, 0, 0)

    #     def lengthOfLIS(self, nums: List[int]) -> int:
    #         dp = {}
    #
    #         def dfs(prev, next):
    #             if next == len(nums):
    #                 return 0
    #             if (prev, next) in dp:
    #                 return dp[(prev, next)]
    #             include = 0
    #             if prev == -1 or nums[next] > nums[prev]:
    #                 include = 1 + dfs(next, next + 1)
    #             exclude = dfs(prev, next + 1)
    #             res = max(include, exclude)
    #             dp[(prev, next)] = res
    #             return res
    #
    #         return dfs(-1, 0)

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


sol = Solution()
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))
