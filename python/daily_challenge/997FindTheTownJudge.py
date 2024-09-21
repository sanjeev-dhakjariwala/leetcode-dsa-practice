from collections import defaultdict
from typing import *


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hash_map = defaultdict(list)

        for t in trust:
            if t[0] not in hash_map:
                hash_map[t[0]] = []
            hash_map[t[0]].append(t[1])
        target = None
        for i in range(1, n + 1):
            if i not in hash_map:
                target = i
        print(hash_map)
        for key, val in hash_map.items():
            if target not in val:
                return -1
        return target if target else -1


sol = Solution()
print(sol.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
