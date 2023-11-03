class Solution:
    def climbStairs(self, n: int) -> int:
        # recursive
        """ if n == 1:
            return 1
        if n == 2:
            return 2
        ans1 = self.climbStairs(n - 1)
        ans2 = self.climbStairs(n - 2)
        return ans1 + ans2 """
        dp = [-1] * (n + 1)
        print(dp)
        def helper(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if dp[n] != -1:
                return dp[n]
            ans1 = helper(n - 1)
            ans2 = helper(n - 2)
            dp[n] = ans1 + ans2
            return dp[n]
        helper(n)
        print(dp)
        return dp[n]

sol = Solution()
print(sol.climbStairs(5))