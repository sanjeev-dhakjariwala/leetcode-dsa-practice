from typing import *


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        c = 0
        n = len(hours)
        curr_sum = 0
        i = 0
        while i < n:
            curr_sum += hours[i]
            if curr_sum % 24 == 0:
                c += 1
            if i % 2 != 0:
                curr_sum = 0
            i += 1
        return c


sol = Solution()
hours = [24, 1]
print(sol.countCompleteDayPairs(hours))
