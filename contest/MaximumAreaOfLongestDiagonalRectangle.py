from typing import *


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diag = float(0)
        for dim in dimensions:
            if max_diag < (dim[0] ** 2 + dim[1] ** 2) ** 0.5:
                max_diag = (dim[0] ** 2 + dim[1] ** 2) ** 0.5
                max_area = dim[0] * dim[1]

        return max_area


sol = Solution()
print(sol.areaOfMaxDiagonal([[6, 5], [8, 6], [2, 10], [8, 1], [9, 2], [3, 5], [3, 5]]))
