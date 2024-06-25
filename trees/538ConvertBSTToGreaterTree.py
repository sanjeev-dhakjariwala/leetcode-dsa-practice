from typing import *
from TreeNode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0

        def helper(root):
            if not root:
                return 0
            helper(root.right)
            self.s += root.val
            root.val = self.s
            helper(root.left)

        helper(root)
        return root


root = deserialize("4,1,6,0,2,5,7,null,null,null,3,null,null,null,8")
sol = Solution()
sol.convertBST(root)
