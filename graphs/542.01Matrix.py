from typing import *
import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # if not mat or not mat[0]:
        #     return mat

        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        queue = collections.deque()

        # Add all cells with value 0 to the queue and mark them as visited.
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))  # (row, col, distance)
                else:
                    mat[i][j] = float("inf")  # Mark non-zero cells with infinity

        while queue:
            row, col, distance = queue.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and mat[new_row][new_col] > distance + 1
                ):
                    mat[new_row][new_col] = distance + 1
                    queue.append((new_row, new_col, distance + 1))

        return mat


sol = Solution()
print(sol.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
