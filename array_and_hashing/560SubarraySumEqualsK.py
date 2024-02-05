from typing import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_freq = {0: 1}  # Initialize with sum 0 and frequency 1
        curr_sum = 0

        for num in nums:
            curr_sum += num
            # Check if there exists a subarray with sum equal to k
            if curr_sum - k in sum_freq:
                count += sum_freq[curr_sum - k]
            # Update the frequency of current sum
            sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

        return count


sol = Solution()
print(sol.subarraySum([1, 2, 3], 3))
