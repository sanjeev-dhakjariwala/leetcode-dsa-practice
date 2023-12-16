from typing import *


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        def helper(i, j, old_col):
            if i < 0 or i >= m or j < 0 or j >= n or image[i][j] != old_col:
                return
            print(f"Changing color at ({i}, {j}) from {old_col} to {color}")
            image[i][j] = color
            helper(i + 1, j, old_col)
            helper(i - 1, j, old_col)
            helper(i, j + 1, old_col)
            helper(i, j - 1, old_col)

        if image[sr][sc] == color:
            return image
        helper(sr, sc, image[sr][sc])
        return image


sol = Solution()
print(sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
print(sol.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
