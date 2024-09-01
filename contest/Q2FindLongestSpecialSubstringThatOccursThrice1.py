from typing import *
from collections import *

class Solution:
    def maximumLength(self, s: str) -> int:
        res = []
        n = len(s)
        def helper(end, temp):
            if end >= n:
                res.append("".join(temp))
                return
            res.append("".join(temp))
            for i in range(end, n):
                temp.append(s[i])
                helper(i + 1, temp)
                temp.pop()

        helper(0, [])
        hash_map = defaultdict(int)
        c = 0
        print(res)
        for r in res:
            hash_map[r] += 1
            if hash_map[r] == 3:
                c += 1
        
        return c if c > 0 else -1

sol = Solution()
s = "abc"
print(sol.maximumLength(s))