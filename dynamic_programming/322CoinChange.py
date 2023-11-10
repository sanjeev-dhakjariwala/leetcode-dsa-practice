class Solution:
    def coinChange(self, coins, amount):
        def recursive_helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if dp[amount] != -1:
                return dp[amount]
            min_coins = float("inf")
            for coin in coins:
                subproblem = recursive_helper(amount - coin)
                if subproblem != float("inf"):
                    min_coins = min(min_coins, subproblem + 1)
            dp[amount] = min_coins
            return min_coins

        dp = [-1] * (amount + 1)
        result = recursive_helper(amount)
        return result if result != float("inf") else -1
