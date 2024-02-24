class Solution:
    def backtrack(self, i, j, row, col, matrix, path):

        if i < 0 or i >= row or j < 0 or j >= col or matrix[i][j] != 1:
            return

        if i == row - 1 and j == col - 1:
            print(path)
        matrix[i][j] = 'X'
        self.backtrack(i + 1, j, row, col, matrix, path + "D")
        self.backtrack(i - 1, j, row, col, matrix, path + "U")
        self.backtrack(i, j - 1, row, col, matrix, path + "L")
        self.backtrack(i, j + 1, row, col, matrix, path + "R")
        matrix[i][j] = 1

sol = Solution()
matrix = [
    [
        1,
        1,
        1,
    ],
    [1, 1, 1],
    [1, 1, 1],
]
sol.backtrack(0, 0, 3, 3, matrix, "")
