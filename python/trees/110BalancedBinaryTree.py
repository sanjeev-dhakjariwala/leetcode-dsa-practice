from typing import Optional
from TreeNode import *

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        height = self.height(root.left) - self.height(root.right)
        if abs(height) > 1:
            return False
        ans1 = self.isBalanced(root.left)
        ans2 = self.isBalanced(root.right)
        return ans1 and ans2
    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return 1 + max(left, right)


""" root = deserialize("1,null,2,null,3")
sol = Solution()
print(sol.isBalanced(root)) """
root = deserialize("3,9,20,null,null,15,7")
sol = Solution()
print(sol.isBalanced(root))
