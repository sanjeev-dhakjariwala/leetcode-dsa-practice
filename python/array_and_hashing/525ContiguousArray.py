from typing import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1
            if prefix_sum in hash_map:
                max_len = max(max_len, i - hash_map[prefix_sum])
            else:
                hash_map[prefix_sum] = i

        return max_len


sol = Solution()
nums = [0, 1, 0]
print(sol.findMaxLength(nums))
