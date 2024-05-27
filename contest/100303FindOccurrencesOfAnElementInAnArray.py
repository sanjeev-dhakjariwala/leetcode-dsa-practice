from collections import defaultdict
from typing import *


class Solution:
    def occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        hash_map = defaultdict(list)

        for i, num in enumerate(nums):
            hash_map[num].append(i)

        print(hash_map)
        pos = hash_map[x]
        res = []
        for query in queries:
            if query - 1 < len(pos):
                res.append(pos[query - 1])
            else:
                res.append(-1)
        return res


sol = Solution()
nums = [1, 3, 1, 7]
queries = [1, 3, 2, 4]
x = 1
print(sol.occurrencesOfElement(nums, queries, x))
