from TreeNode import *
class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root or root.val == p.val or root.val == q.val:
            return root

        # Recursively search in the left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both p and q are found in different subtrees, the current node is the LCA
        if left_lca and right_lca:
            return root

        # If either p or q is found, return that node as a potential LCA
        return left_lca if left_lca else right_lca
