class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(i, j, m, n):
            if i == m - 1 and j == n - 1:
                return 1
            if i >= m or j >= n or i < 0 or j < 0:
                return 0

            ans1 = helper(i + 1, j, m, n)
            ans2 = helper(i, j + 1, m, n)
            return ans1 + ans2

        return helper(0, 0, m, n)

sol = Solution()
print(sol.uniquePaths(3, 7))