from typing import *


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash_set = {}
        n = len(grid)
        for i in range(n * n):
            val = i + 1
            hash_set[val] = 0
        res = []
        for i in range(n):
            for j in range(n):
                if not hash_set[grid[i][j]]:
                    hash_set[grid[i][j]] = 1
                else:
                    res.append(grid[i][j])
        print(res)
        return res


sol = Solution()
print(sol.findMissingAndRepeatedValues([[1, 3], [2, 2]]))
