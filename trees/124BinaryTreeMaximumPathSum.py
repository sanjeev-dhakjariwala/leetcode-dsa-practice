# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import *
from TreeNode import *


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            self.max_sum = max(self.max_sum, root.val + left, right)
            return root.val + max(left, right)

        helper(root)
        return self.max_sum


sol = Solution()
root = deserialize("1,2,3")
print(sol.maxPathSum(root))
