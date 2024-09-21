from typing import *


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_visited = [[False] * cols for _ in range(rows)]
        atlantic_visited = [[False] * cols for _ in range(rows)]
        result = []

        # Define DFS function to mark cells reachable from ocean
        def dfs(r, c, visited):
            visited[r][c] = True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < rows
                    and 0 <= new_c < cols
                    and not visited[new_r][new_c]
                    and heights[new_r][new_c] >= heights[r][c]
                ):
                    dfs(new_r, new_c, visited)

        # DFS from cells adjacent to the Pacific Ocean (top and left edges)
        for i in range(rows):
            dfs(i, 0, pacific_visited)
        for j in range(cols):
            dfs(0, j, pacific_visited)

        # DFS from cells adjacent to the Atlantic Ocean (bottom and right edges)
        for i in range(rows):
            dfs(i, cols - 1, atlantic_visited)
        for j in range(cols):
            dfs(rows - 1, j, atlantic_visited)
        print(atlantic_visited)
        print(pacific_visited)

        # Find the intersection of cells reachable from both oceans
        for i in range(rows):
            for j in range(cols):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    result.append([i, j])

        return result


sol = Solution()
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
print(sol.pacificAtlantic(heights))

"""
[
    [True, True, True, True, True],
    [True, True, True, True, True],
    [True, True, True, False, False],
    [True, True, False, False, False],
    [True, False, False, False, False]
]
[
    [False, False, False, False, True],
    [False, False, False, True, True],
    [False, False, True, True, True],
    [True, True, True, True, True],
    [True, True, True, True, True]
]

"""
