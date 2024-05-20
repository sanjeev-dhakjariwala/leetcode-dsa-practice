from typing import *


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        if n == 1:
            return [True] * len(queries)

        def helper(arr):
            res = []

            for num in nums:
                if num % 2 == 0:
                    res.append(0)
                else:
                    res.append(1)

            for i in range(len(res) - 1):
                if res[i] == res[i + 1]:
                    return False

            return True

        ans = []
        for query in queries:
            ans.append(helper(nums[query[0] : query[1] + 1]))

        return ans


sol = Solution()
nums = [3, 7, 8]
query = [[0, 2]]
print(sol.isArraySpecial(nums, query))
