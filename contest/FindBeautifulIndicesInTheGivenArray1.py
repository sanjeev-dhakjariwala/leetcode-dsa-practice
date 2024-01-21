from typing import *


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        b_index = -1
        res = []
        for i in range(len(s)):
            # if s[i: i + len(b)] == b:
            #     b_index = i
            if s[i : i + len(a)] == a:
                for i in range(len(s)):
                    if s[i : i + len(b)] == b:
                        b_index = i
                if b_index != -1 and abs(i - b_index) <= k:
                    res.append(i)
                    b_index = -1

        return res


sol = Solution()
print(sol.beautifulIndices("isawsquirrelnearmysquirrelhouseohmy", "my", "squirrel", 15))
