from typing import *

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        # Step 2: Reverse each row
        for i in range(n):
            matrix[i].reverse()

sol = Solution()
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sol.rotate(arr)
print(arr)
