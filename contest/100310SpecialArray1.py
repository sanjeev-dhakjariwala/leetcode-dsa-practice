from typing import *

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        n = len(nums)
        if n == 1:
            return True
        res = []

        for num in nums:
            if num % 2 == 0:
                res.append(0)
            else:
                res.append(1)
        print(res)
        for i in range(len(res) - 1):
            if res[i] == res[i + 1]:
                return False

        return True
        """
        n = len(nums)
        if n == 1:
            return True

        for i in range(1, n - 1):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False

        return True


sol = Solution()
nums = [1, 5]
print(sol.isArraySpecial(nums))
