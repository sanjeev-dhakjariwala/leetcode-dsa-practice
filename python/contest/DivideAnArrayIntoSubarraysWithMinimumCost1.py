from typing import *


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        res = []

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_array = nums[i : j + 1]
                res.append(sub_array[:])
        min_res = float("inf")
        print(res)
        for i in range(0, len(res) - 3):
            temp_sum = 0
            for j in range(i, i + 3):
                temp_sum += res[j][0]
            min_res = min(min_res, temp_sum)

        return min_res


sol = Solution()
print(sol.minimumCost([1, 2, 3, 12]))
