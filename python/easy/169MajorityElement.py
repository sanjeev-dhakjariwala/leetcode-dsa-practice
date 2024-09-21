from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = res = 0

        for num in nums:
            if count == 0:
                res = num
            count += 1 if res == num else -1

        return res


sol = Solution()
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
