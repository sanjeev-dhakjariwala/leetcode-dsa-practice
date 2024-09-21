from typing import *


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for n in arr:
            prev = min(prev + 1, n)
        return prev


sol = Solution()
print(sol.maximumElementAfterDecrementingAndRearranging([2, 2, 1, 2, 1]))
