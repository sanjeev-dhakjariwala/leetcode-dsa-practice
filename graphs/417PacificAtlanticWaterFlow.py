from typing import *

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(r, c, reachable):
            reachable.add((r, c))

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m
                    and 0 <= nc < n
                    and (nr, nc) not in reachable
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, reachable)

        # DFS from the left and top edges (Pacific Ocean)
        for i in range(m):
            dfs(i, 0, pacific_reachable)
        for j in range(n):
            dfs(0, j, pacific_reachable)

        # DFS from the right and bottom edges (Atlantic Ocean)
        for i in range(m):
            dfs(i, n - 1, atlantic_reachable)
        for j in range(n):
            dfs(m - 1, j, atlantic_reachable)

        # Find the cells that are reachable from both oceans
        result = list(pacific_reachable.intersection(atlantic_reachable))

        return result
