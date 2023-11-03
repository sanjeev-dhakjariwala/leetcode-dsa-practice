from pyparsing import Optional
from trees.TreeNode import TreeNode


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