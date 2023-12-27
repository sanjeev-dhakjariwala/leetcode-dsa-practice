from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False


sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 1]))
