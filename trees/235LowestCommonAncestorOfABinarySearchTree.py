from typing import *
from TreeNode import *


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        while True:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root


root = deserialize("6,2,8,0,4,7,9,null,null,3,5")
sol = Solution()
p = TreeNode(2)
p.left = None
p.right = None
q = TreeNode(4)
q.left = None
q.right = None
print(sol.lowestCommonAncestor(root, p, q).val)
