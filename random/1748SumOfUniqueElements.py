from typing import *


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        numSet = {}
        s = 0
        for num in nums:
            numSet[num] = 1 + numSet.get(num, 0)

        for key, value in numSet.items():
            if value == 1:
                s += key
        return s


sol = Solution()
print(sol.sumOfUnique([1, 2, 3, 2]))
