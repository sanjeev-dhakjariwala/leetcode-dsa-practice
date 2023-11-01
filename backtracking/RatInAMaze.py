class Solution:
    def findPath(self, maze, n):
        # code here
        ans = []
        def helper(maze, i, j, n, path):
            if i > n or j > n:
                return
            if i == n and j == n:
                print(path)
                ans.append(path)
                return
            helper(maze, i + 1, j, n, path + "D")
            path.pop()
            helper(maze, i, j + 1, n, path + "R")
        helper(maze, 0, 0, n, "")
        return ans