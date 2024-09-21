from typing import *
from collections import *


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        prefix_sum = 0
        c = 0

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum - goal in hash_map:
                c += hash_map[prefix_sum - goal]

            hash_map[prefix_sum] += 1

        return c


sol = Solution()
nums = [1, 0, 1, 0, 1]
print(sol.numSubarraysWithSum(nums, 2))
