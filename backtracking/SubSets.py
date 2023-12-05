from typing import *


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = []
    #     subSet = []

    #     def dfs(i):
    #         if i == len(nums):
    #             res.append(subSet.copy())
    #             return
    #         subSet.append(nums[i])
    #         dfs(i + 1)
    #         subSet.pop()
    #         dfs(i + 1)

    #     dfs(0)
    #     return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, t):
            if i == n:
                res.append(t[:])
                return
            res.append(t[:])
            for j in range(i, n):
                t.append(nums[j])
                dfs(j + 1, t)
                t.pop()

        dfs(0, [])
        return res


sol = Solution()
print(sol.subsets([3, 5, 6]))
