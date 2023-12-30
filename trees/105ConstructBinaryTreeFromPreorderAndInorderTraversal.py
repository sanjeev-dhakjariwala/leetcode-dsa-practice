from TreeNode import *
from typing import *


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index + 1 :])

        return root


sol = Solution()
root = sol.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

