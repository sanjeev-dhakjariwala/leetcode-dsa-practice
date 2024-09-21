# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from TreeNode import *


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, min_val, max_val):
            if not root:
                return True
            if root.val >= max_val:
                return False
            if root.val <= min_val:
                return False
            left = helper(root.left, min_val, root.val)
            right = helper(root.right, root.val, max_val)

            return left and right

        return helper(root, float('-inf'), float('inf'))


sol = Solution()
root = deserialize("2,1,3")
print(sol.isValidBST(root))
