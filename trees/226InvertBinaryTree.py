from typing import Optional
from trees.TreeNode import TreeNode
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        temp = left
        root.left = right
        root.right = temp
        return root
