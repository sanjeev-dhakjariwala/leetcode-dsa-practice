from typing import *

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result

sol = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
print(sol.combinationSum2(candidates, target))
