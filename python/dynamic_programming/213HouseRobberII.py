from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_helper(nums, start, end, memo):
            if start > end:
                return 0
            if start == end:
                return nums[start]
            if memo[start] != -1:
                return memo[start]
            rob_start = nums[start] + rob_helper(nums, start + 2, end, memo)
            skip_start = rob_helper(nums, start + 1, end, memo)
            memo[start] = max(rob_start, skip_start)
            return memo[start]

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            # Initialize memoization arrays
            memo1 = [-1] * n
            memo2 = [-1] * n
            # Calculate the maximum amount by considering two cases:
            # 1. Rob the first house and exclude the last one.
            # 2. Exclude the first house and rob the last one.
            max1 = rob_helper(nums, 0, n - 2, memo1)
            max2 = rob_helper(nums, 1, n - 1, memo2)
            return max(max1, max2)
