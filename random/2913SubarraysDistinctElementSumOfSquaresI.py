from typing import *


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            distinct_count_set = []
            for j in range(i, n):
                distinct_count_set.append(nums[j])
                print(distinct_count_set)
                distinct_count = len(distinct_count_set)
                result += distinct_count**2
        return result


sol = Solution()
print(sol.sumCounts([1, 2, 1]))
