from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        low, high = 0, (row * col) - 1

        while low <= high:
            mid = low + (high - low) // 2
            midValue = matrix[mid // col][mid % col]
            if target == midValue:
                return True
            elif midValue < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


sol = Solution()
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 31))
