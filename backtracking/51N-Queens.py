from typing import *


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check if there is a queen in the same column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # Check if there is a queen in the left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # Check if there is a queen in the right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == "Q":
                    return False

            return True

        def backtrack(row):
            if row == n:
                solutions.append(["".join(row) for row in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        solutions = []
        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0)
        return solutions

sol = Solution()
print(sol.solveNQueens(4))