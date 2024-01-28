from typing import *


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)

        for i in range(1, n + 1):
            t = i
            c = 0
            while t != 0:
                r = t % 2
                if r == 1:
                    c += 1
                t = t // 2
            res[i] = c

        return res

sol = Solution()
print(sol.countBits(5))