from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(temp, s):
            if s == 0:
                res.append(temp[:])
                return
            if s < 0:
                return

            for c in candidates:
                temp.append(c)
                helper(temp, s - c)
                temp.pop()

        helper([], target)
        return res

sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))