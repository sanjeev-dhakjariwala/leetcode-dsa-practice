# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from TreeNode import *
from typing import *


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:

        def helper(root, level, child):
            if not root:
                return
            if level + 1 == depth:
                temp = None
                if child == "left":
                    temp = root.left
                else:
                    temp = root.right
                node = TreeNode(val)
                if child == "left":
                    root.left = node
                    node.left = temp
                else:
                    root.right = node
                    node.right = temp
            helper(root.left, level + 1, "left")
            helper(root.right, level + 1, "right")

        helper(root, 1, "left")
        return root


sol = Solution()
root = deserialize("[4,2,6,3,1,5]")
inorder_traversal(root)
sol.addOneRow(root, 1, 2)
