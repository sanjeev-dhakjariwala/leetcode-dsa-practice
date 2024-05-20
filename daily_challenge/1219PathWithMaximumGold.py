from typing import *


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_ans = float("-inf")

        def dfs(i, j, curr_sum):
            nonlocal max_ans
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == float("-inf"):
                return 0
            temp = grid[i][j]
            curr_sum += grid[i][j]
            grid[i][j] = float("-inf")
            up = dfs(i - 1, j, curr_sum)
            down = dfs(i + 1, j, curr_sum)
            left = dfs(i, j + 1, curr_sum)
            right = dfs(i, j - 1, curr_sum)
            max_ans = max(max_ans, (up + down + left + right))
            grid[i][j] = temp
            return up + down + left + right

        for i in range(rows):
            for j in range(cols):
                dfs(i, j, 0)

        return max_ans


sol = Solution()
grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
print(sol.getMaximumGold(grid))
