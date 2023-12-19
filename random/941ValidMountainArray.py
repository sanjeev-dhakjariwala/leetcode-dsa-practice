from typing import *


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        i = 0
        is_dec = False
        while i < n - 1:
            if arr[i + 1] > arr[i]:
                is_dec = True
                i += 1
                break
            i += 1

        while i < n - 1:
            if arr[i] <= arr[i + 1]:
                is_dec = False
            i += 1

        return is_dec


sol = Solution()
print(sol.validMountainArray([2, 0, 2]))
