from typing import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        n = len(nums)
        num_set = {}
        for i, num in enumerate(nums):
            if num in num_set and abs(num_set[num] - i) <= k:
                return True
            num_set[num] = i

        return False


sol = Solution()
print(sol.containsNearbyDuplicate([1, 2, 3, 1], 3))
