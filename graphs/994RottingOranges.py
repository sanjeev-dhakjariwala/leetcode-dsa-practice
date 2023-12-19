from typing import *
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if not grid:
        #     return 0

        # m, n = len(grid), len(grid[0])
        # fresh_oranges = 0
        # rotten_oranges = collections.deque()

        # # Count fresh oranges and store the position of rotten oranges
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             fresh_oranges += 1
        #         elif grid[i][j] == 2:
        #             rotten_oranges.append((i, j, 0))

        # # Define 4-directional neighbors
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # minutes_elapsed = 0

        # while rotten_oranges:
        #     i, j, minutes_elapsed = rotten_oranges.popleft()

        #     for di, dj in directions:
        #         ni, nj = i + di, j + dj
        #         if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
        #             grid[ni][nj] = 2
        #             fresh_oranges -= 1
        #             rotten_oranges.append((ni, nj, minutes_elapsed + 1))

        # return minutes_elapsed if fresh_oranges == 0 else -1
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        rotten_oranges = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                elif grid[i][j] == 2:
                    rotten_oranges.append((i, j, 0))
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        while rotten_oranges:
            i, j, minutes_elapsed = rotten_oranges.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh_oranges -= 1
                    rotten_oranges.append((ni, nj, minutes_elapsed + 1))
        return minutes_elapsed if fresh_oranges == 0 else -1


sol = Solution()
print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
