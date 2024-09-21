from typing import *


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(i, path):
            if i == len(s):
                res.append(path)
                return
            for j in range(i + 1, len(s) + 1):
                t = s[i: j]
                if t == t[::-1]:
                    helper(j, path + [s[i: j]])
        
        res = []
        helper(0, [])
        return res


sol = Solution()
print(sol.partition("aab"))
