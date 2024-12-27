from typing import *


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sumOfDigit(n):
            s = 0
            while n != 0:
                r = n % 10
                s += r
                n /= 10
            return s

        min_num = float("inf")
        for num in nums:
            temp = sumOfDigit(num)
            min_num = min(min_num, temp)
        return min_num


sol = Solution()
arr = [10, 12, 13, 14]
print(sol.minElement(arr))
