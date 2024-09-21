from typing import *


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize dp array with zeros, dp[0] is 1 because there's one way to make amount 0
        dp = [0] * (amount + 1)
        dp[0] = 1

        # Iterate over each coin
        for coin in coins:
            # Update dp array for each amount from coin to the target amount
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        # Return the number of ways to make the target amount
        return dp[amount]


sol = Solution()
amount = 5
coins = [1, 2, 5]
print(sol.change(amount, coins))
