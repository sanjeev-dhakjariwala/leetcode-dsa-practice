from trees.TreeNode import *
from typing import *


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root or targetSum == 0:
            return False

        def helper(root, targetSum):
            if targetSum == 0 and not root:
                return True
            if not root:
                return False

            left = helper(root.left, targetSum - root.val)
            right = helper(root.right, targetSum - root.val)
            return left or right

        return helper(root, targetSum)


sol = Solution()
root = deserialize("1,2")
print(sol.hasPathSum(root, 1))