class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # Initialize a 2D table with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: empty string t is a subsequence of any string s
        for i in range(m + 1):
            dp[i][0] = 1

        # Fill the dp table using the recurrence relation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + (s[i - 1] == t[j - 1]) * dp[i - 1][j - 1]
        print(dp)
        return dp[m][n]


sol = Solution()
print(sol.numDistinct("rabbbit", "rabbit"))
