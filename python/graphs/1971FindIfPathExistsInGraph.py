from typing import *
from collections import *


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adjacency_list = defaultdict(list)
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        print(adjacency_list)
        # Initialize visited set and queue for BFS
        visited = set()
        queue = deque([source])

        # Perform BFS
        while queue:
            current = queue.popleft()
            visited.add(current)
            if current == destination:
                return True
            for neighbor in adjacency_list[current]:
                if neighbor not in visited:
                    queue.append(neighbor)

        return False


sol = Solution()
edges = [[0, 1], [1, 2], [2, 0]]
print(sol.validPath(3, edges, 0, 2))
