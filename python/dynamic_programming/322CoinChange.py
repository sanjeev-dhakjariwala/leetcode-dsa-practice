from typing import List


class Solution:
    def coinChange(self, coins, amount):
        def recursive_helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")

            min_coins = float("inf")
            for coin in coins:
                subproblem = recursive_helper(amount - coin)
                if subproblem != float("inf"):
                    min_coins = min(min_coins, subproblem + 1)

            return min_coins

        result = recursive_helper(amount)
        return result if result != float("inf") else -1

sol = Solution()
print(sol.coinChange([1, 2, 5], 11))
