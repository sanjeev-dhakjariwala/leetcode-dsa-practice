from typing import *
from collections import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, node):
            while parent[node] != node:
                node = parent[node]
            return node

        def union(parent, rank, u, v):
            root_u = find(parent, u)
            root_v = find(parent, v)
            if root_u == root_v:
                return False  # Cycle detected
            if rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            elif rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return True

        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)
        redundant_edge = []

        for u, v in edges:
            if not union(parent, rank, u, v):
                redundant_edge = [u, v]

        return redundant_edge
