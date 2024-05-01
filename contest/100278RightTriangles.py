from typing import *

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        c = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if i + 1 < rows and j + 1 < cols:
                    if (
                        grid[i][j] == 1
                        and grid[i + 1][j] == 1
                        and grid[i + 1][j + 1] == 1
                    ):
                        c += 1
        return c

sol = Solution()
grid = [[0, 1, 0], [0, 1, 1], [0, 1, 0]]
print(sol.numberOfRightTriangles(grid))
