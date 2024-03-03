from typing import *
from collections import *


class Solution:
    def islandsAndTreasureDFS(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Up, down, right, left

        def dfs(row, col, distance):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] < distance
            ):
                # Out of bounds or already has a shorter distance
                return

            grid[row][col] = distance
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                # Explore neighbors with increased distance
                dfs(new_row, new_col, distance + 1)

        # Find gates and start exploration
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    dfs(row, col, 0)

    def islandsAndTreasureBFS(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows, cols = len(grid), len(grid[0])
        gates = deque()

        # Find all gate locations and enqueue them
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    gates.append((i, j, 0))

        # Perform BFS from each gate
        while gates:
            row, col, distance = gates.popleft()

            # Explore four directions
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and grid[new_row][new_col] == 2147483647
                ):
                    grid[new_row][new_col] = distance + 1
                    gates.append((new_row, new_col, distance + 1))


sol = Solution()
grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
sol.islandsAndTreasureDFS(grid)
print(grid)