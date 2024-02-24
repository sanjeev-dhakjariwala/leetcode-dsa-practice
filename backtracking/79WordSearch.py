from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, index, processed):
            if 0 <= i < m and 0 <= j < n and index < len(word):
                ans1 = dfs(i + 1, j, index + 1, processed + board[i][j])
                ans2 = dfs(i, j + 1, index + 1, processed + board[i][j])
                ans3 = dfs(i - 1, j, index + 1, processed + board[i][j])
                ans4 = dfs(i, j - 1, index + 1, processed + board[i][j])

                return ans1 or ans2 or ans3 or ans4
            elif 0 <= i < m and 0 <= j < n and index == len(word) and processed == word:
                return True
            else:
                return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0, ""):
                    return True

        return False


sol = Solution()
print(
    sol.exist(
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
    )
)
