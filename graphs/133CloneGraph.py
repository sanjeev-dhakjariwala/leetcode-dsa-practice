from typing import Optional
from Node import *


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None


graph = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
sol = Solution()
new_graph = sol.cloneGraph(graph)
print(print_graph(new_graph))