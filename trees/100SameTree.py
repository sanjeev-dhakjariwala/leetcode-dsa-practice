from pyparsing import Optional
from trees.TreeNode import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        ans1 = self.isSameTree(p.left, q.left)
        ans2 = self.isSameTree(p.right, q.right)
        return ans1 and ans2