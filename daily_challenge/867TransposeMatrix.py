from typing import *


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[] for i in range(len(matrix[0]))]
        print(res)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res[j].append(matrix[i][j])
        return res


sol = Solution()
print(sol.transpose([[1, 2, 3], [4, 5, 6]]))
print(sol.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
