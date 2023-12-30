from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxLeft, maxRight = height[0], height[n - 1]
        i, j = 0, n - 1
        max_area = 0

        while i < j:
            max_area = max(max_area, min(maxLeft, maxRight) * (j - i))
            if maxLeft < height[i]:
                maxLeft = height[i]
                i += 1
            elif maxRight < height[j]:
                maxLeft = height[i]
                j -= 1
            else:
                i += 1
                j -= 1

        return max_area


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
