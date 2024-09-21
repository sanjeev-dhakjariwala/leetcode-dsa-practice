from typing import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_length = 0
        running_sum = 0
        sum_index_map = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                running_sum -= 1
            else:
                running_sum += 1

            if running_sum in sum_index_map:
                max_length = max(max_length, i - sum_index_map[running_sum])
            else:
                sum_index_map[running_sum] = i

        return max_length


sol = Solution()
print(sol.findMaxLength([0, 1]))
