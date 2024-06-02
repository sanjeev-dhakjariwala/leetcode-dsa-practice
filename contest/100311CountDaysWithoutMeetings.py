from collections import defaultdict
from typing import *


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        arr = defaultdict(bool)
        c = 0

        def helper(start, end):
            while start <= end:
                if not start in arr:
                    arr[start] = True
                start += 1

        for meeting in meetings:
            helper(meeting[0], meeting[1])

        for i in range(1, days + 1):
            if not i in arr:
                c += 1
        return c


sol = Solution()
days = 6
meetings = [[1,6]]
print(sol.countDays(days, meetings))
