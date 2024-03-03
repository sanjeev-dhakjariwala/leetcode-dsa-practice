from typing import *
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        fresh_count = 0
        rotten_queue = collections.deque()
        
        # Find initial rotten oranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i, j, 0))  # (row, col, minutes)
        
        minutes = 0
        while rotten_queue:
            row, col, minutes = rotten_queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2  # Mark the fresh orange as rotten
                    fresh_count -= 1
                    rotten_queue.append((new_row, new_col, minutes + 1))
        
        return minutes if fresh_count == 0 else -1


sol = Solution()
print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
