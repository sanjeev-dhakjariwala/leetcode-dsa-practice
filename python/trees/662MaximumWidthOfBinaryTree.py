from TreeNode import *
from typing import *
import collections


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = collections.deque([(root, 0)])  # (node, position)

        while queue:
            level_size = len(queue)
            _, left_pos = queue[0]

            for i in range(level_size):
                node, pos = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))

            max_width = max(max_width, pos - left_pos + 1)

        return max_width


root = deserialize("1,3,2,5,3,null,9")
sol = Solution()
print(sol.widthOfBinaryTree(root))