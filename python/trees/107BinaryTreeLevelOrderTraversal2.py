from trees.TreeNode import *
from typing import *
import collections
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = collections.deque([root])

        while queue:
            level_nodes = []
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.insert(0, level_nodes)  # Insert at the beginning to reverse the order

        return result

root = deserialize("3,9,20,null,null,15,7")
sol = Solution()
print(sol.levelOrderBottom(root))