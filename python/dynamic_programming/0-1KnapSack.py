class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        # code here
        """
        if n == 0 or W == 0:
            return 0
        if wt[n - 1] > W:
            return self.knapSack(W, wt, val, n - 1)
        include = val[n - 1] + self.knapSack(W - wt[n - 1], wt, val, n - 1);
        exclude = self.knapSack(W, wt, val, n - 1);
        return max(include, exclude)
        """

        memo = {}

        def knapSackMemo(W, wt, val, n):
            if (W, n) in memo:
                return memo[(W, n)]
            if n == 0 or W == 0:
                return 0
            if wt[n - 1] > W:
                return knapSackMemo(W, wt, val, n - 1)
            include = val[n - 1] + knapSackMemo(W - wt[n - 1], wt, val, n - 1)
            exclude = knapSackMemo(W, wt, val, n - 1)
            ans = max(include, exclude)
            memo[(W, n)] = ans
            return ans

        return knapSackMemo(W, wt, val, n)
