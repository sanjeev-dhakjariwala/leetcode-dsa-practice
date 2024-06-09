from typing import *


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first occurrence of each remainder
        remainder_dict = {0: -1}
        cumulative_sum = 0

        for i, num in enumerate(nums):
            cumulative_sum += num

            # Calculate the remainder of the cumulative sum with k
            if k != 0:
                remainder = cumulative_sum % k
            else:
                remainder = cumulative_sum

            # If the same remainder has been seen before
            if remainder in remainder_dict:
                # Check if the subarray length is at least 2
                if i - remainder_dict[remainder] > 1:
                    return True
            else:
                # Store the index of the first occurrence of this remainder
                remainder_dict[remainder] = i

        return False


sol = Solution()
nums = [23, 2, 4, 6, 7]
k = 6
print(sol.checkSubarraySum(nums, k))