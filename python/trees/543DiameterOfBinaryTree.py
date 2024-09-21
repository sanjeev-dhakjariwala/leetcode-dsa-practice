from typing import *
from TreeNode import *


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root, diameter):
            if not root:
                return 0
            left = helper(root.left, diameter)
            right = helper(root.right, diameter)
            diameter[0] = max(diameter[0], left + right)
            return 1 + max(left, right)

        diameter = [0]  # Create a list to store the diameter value
        helper(root, diameter)
        return diameter[0]


sol = Solution()
root = deserialize("1,null,2,3,4,5")
print(sol.diameterOfBinaryTree(root))