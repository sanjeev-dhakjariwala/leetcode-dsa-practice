from trees.TreeNode import *
from typing import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = str(root.val)

        if root.left or root.right:
            result += "(" + self.tree2str(root.left) + ")"

        if root.right:
            result += "(" + self.tree2str(root.right) + ")"

        return result


sol = Solution()
root = deserialize("1,2,3,4")
print(sol.tree2str(root))
