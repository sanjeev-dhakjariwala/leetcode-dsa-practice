from TreeNode import *
from typing import *


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(root, isLeft):
            if not root:
                return 0
            
            if not root.left and not root.right:
                if isLeft:
                    return root.val
                return 0

            left = helper(root.left, True)
            right = helper(root.right, False)
            return left + right

        return helper(root, False)


sol = Solution()
root = deserialize("4,2,6,3,1,5")
print(sol.sumOfLeftLeaves(root))
