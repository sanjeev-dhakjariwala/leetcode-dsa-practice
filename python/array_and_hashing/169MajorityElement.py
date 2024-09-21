from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate


sol = Solution()
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
