from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def helper(start, temp):
            if start == n:
                res.append(temp[:])
                return
            res.append(temp[:])
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                helper(i + 1, temp)
                temp.pop()

        res = []
        helper(0, [])
        return res


sol = Solution()
print(sol.subsetsWithDup([1, 2, 2]))
