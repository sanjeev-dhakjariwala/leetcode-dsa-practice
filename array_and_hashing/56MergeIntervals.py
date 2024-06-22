from typing import *


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        merged_intervals = []
        intervals.sort(key=lambda x:x[0])
        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals

sol = Solution()
print(sol.merge([[1, 3], [8, 10], [15, 18], [2, 6]]))
