from TreeNode import *
from typing import *


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def findTarget(root):
            if not root:
                return None
            if root.val == target:
                return root

            left = findTarget(root.left)
            right = findTarget(root.right)
            if left != None and right == None:
                return left
            elif left == None and right != None:
                return right

        def trav(root, idx):
            if not root:
                return
            if root and idx == k:
                res.append(root.val)
                return
            trav(root.left, idx + 1)
            trav(root.right, idx + 1)

        res = []
        new_node = findTarget(root)
        print(new_node)

        if new_node:
            trav(new_node, 0)

        return res


sol = Solution()
root = deserialize("3,5,1,6,2,0,8,null,null,7,4")
sol.distanceK(root, 5, 2)
