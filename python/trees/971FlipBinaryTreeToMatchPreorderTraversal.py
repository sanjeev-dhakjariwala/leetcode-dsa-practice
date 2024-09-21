# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from trees.TreeNode import *
from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.flipped = []
        self.index = 0

        def dfs(node):
            if not node:
                return True

            if node.val != voyage[self.index]:
                return False

            self.index += 1

            if node.left and node.left.val != voyage[self.index]:
                self.flipped.append(node.val)
                return dfs(node.right) and dfs(node.left)

            return dfs(node.left) and dfs(node.right)

        return self.flipped if dfs(root) else [-1]


sol = Solution()
root = deserialize("1,2,3")
print(sol.flipMatchVoyage(root, [1, 3, 2]))
