class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)
        
        # If the total sum is odd, it can't be divided into two equal subsets.
        if total_sum % 2 != 0:
            return False
        
        half_sum = total_sum // 2
        
        # Initialize a 1D array to store whether a sum 'i' can be achieved with the elements in 'nums'.
        dp = [False] * (half_sum + 1)
        print(dp)
        dp[0] = True
        
        # Iterate through the elements in 'nums' and update the 'dp' array.
        for num in nums:
            for i in range(half_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[half_sum]

sol = Solution()
print(sol.canPartition([1,5,11,5]))