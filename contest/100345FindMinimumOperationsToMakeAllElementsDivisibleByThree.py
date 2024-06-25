from typing import *


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def plusOneOrMinusOne(num, operation):
            c = 0
            while True:
                c += 1
                if operation == "+":
                    num += 1
                else:
                    num -= 1
                if num % 3 == 0:
                    break
            return c

        c = 0
        for num in nums:
            if num % 3 == 0:
                continue
            c += min(plusOneOrMinusOne(num, "+"), plusOneOrMinusOne(num, "-"))
        return c


sol = Solution()
nums = [3, 6, 9]
print(sol.minimumOperations(nums))
