class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val):
        n = len(wt)
        self.max_sum = float("-inf")

        def helper(level, curr_weight, curr_val):
            if level == n:
                return
            if curr_weight >= W:
                return
            for i in range(level, n):
                if wt[i] <= W and curr_weight + wt[i] <= W:
                    curr_weight += wt[i]
                    curr_val += val[i]
                    self.max_sum = max(self.max_sum, curr_val)
                    helper(i + 1, curr_weight, curr_val)
                    # curr_weight -= wt[i]
                    curr_val -= val[i]

        helper(0, 0, 0)
        return self.max_sum if self.max_sum != float("-inf") else 0


sol = Solution()
W = 3
val = [1, 2, 3]
wt = [4, 5, 1]
print(sol.knapSack(W, wt, val))
