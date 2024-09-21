from typing import *
from trees.TreeNode import *


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []

        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)
        print(arr)
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] + arr[j] == k:
                return True
            elif arr[i] + arr[j] > k:
                j -= 1
            else:
                i += 1
        return False


""" root = deserialize("1,null,2,null,3")
sol = Solution()
print(sol.isBalanced(root)) """
root = deserialize("5,3,6,2,4,null,7")
sol = Solution()
print(sol.findTarget(root, 7))
