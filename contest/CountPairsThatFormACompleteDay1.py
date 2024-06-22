from typing import *


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        n = len(hours)
        c = 0

        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    c += 1
        return c


sol = Solution()
hours = [24, 24, 24, 24]
print(sol.countCompleteDayPairs(hours))
