from typing import (
    List,
)
from collections import defaultdict


class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """

    def count_components(self, n: int, edges: List[List[int]]) -> int:
        # write your code here
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        graph = defaultdict(list)
        visited = set()

        # Build the adjacency list representation of the graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)

        return count
