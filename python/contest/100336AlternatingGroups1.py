from typing import *


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        c = 0
        n = len(colors)

        for i in range(n):
            print(colors[i - 1], colors[i], colors[(i + 1) % n])
            if colors[i - 1] != colors[i] and colors[i] != colors[(i + 1) % n]:
                c += 1
        return c


sol = Solution()
colors = [0, 1, 0, 0, 1]
print(sol.numberOfAlternatingGroups(colors))
