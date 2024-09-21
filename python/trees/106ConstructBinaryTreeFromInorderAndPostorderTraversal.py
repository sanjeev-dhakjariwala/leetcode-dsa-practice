from TreeNode import *
from typing import *

class Solution:
    def buildTree(self, inorder: List[int], postorder:List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        node = TreeNode(root_val)
        index = inorder.index(root_val)

        node.left = self.buildTree(inorder[index + 1], postorder)
        node.right = self.buildTree(inorder[: index - 1], postorder)

        return node
