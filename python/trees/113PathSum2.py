from trees.TreeNode import *
from typing import *


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def helper(root, t_sum, temp):
            if not root:
                return
            if not root.left and not root.right:
                if t_sum == root.val:
                    res.append(temp[:])
                    temp.pop()
                    return
            temp.append(root.val)
            helper(root.left, t_sum - root.val, temp)
            helper(root.right, t_sum - root.val, temp)

        helper(root, targetSum, [])
        return res


sol = Solution()
root = deserialize("5,4,8,11,null,13,4,7,2,null,null,5,1")
print(sol.pathSum(root, 22))
