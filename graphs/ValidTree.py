from typing import *

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    if neighbor in visited or not dfs(neighbor, node):
                        return False
            return True

        if len(edges) != n - 1:
            return False  # Not enough edges for a connected graph

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        if not dfs(0, -1):  # Start DFS from node 0
            return False

        return len(visited) == n  # Check if all nodes are visited
