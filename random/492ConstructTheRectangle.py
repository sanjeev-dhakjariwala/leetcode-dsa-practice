from typing import *


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for L in range(int(area ** 0.5), 0, -1):
            if area % L == 0:
                W = area // L
                return [max(L, W), min(L, W)]


sol = Solution()
print(sol.constructRectangle(122122))
