# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from trees.TreeNode import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.check(root, subRoot):
            return True
        ans1 = self.isSubtree(root.left, subRoot)
        ans2 = self.isSubtree(root.right, subRoot)
        return ans1 or ans2

    def check(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        ans1 = self.check(root.left, subRoot.left)
        ans2 = self.check(root.right, subRoot.right)
        return ans1 and ans2
