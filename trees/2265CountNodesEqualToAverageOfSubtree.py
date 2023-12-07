from math import ceil

from trees.TreeNode import *
import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def sumOfTree(root):
            if not root:
                return 0
            left = sumOfTree(root.left)
            right = sumOfTree(root.right)
            return root.val + left + right

        def countNodes(root):
            if not root:
                return 0
            left = countNodes(root.left)
            right = countNodes(root.right)
            return 1 + left + right

        def calTree(root):
            if not root:
                return
            sub_tree_sum1 = sumOfTree(root)
            c = countNodes(root)
            if root.val == math.floor((sub_tree_sum1 / c)):
                nonlocal res
                res += 1
            calTree(root.left)
            calTree(root.right)

        res = 0
        calTree(root)
        return res

        res = 0
        calTree(root)
        return res


sol = Solution()
root = deserialize("1,null,3,null,1,null,3")
print(sol.averageOfSubtree(root))
