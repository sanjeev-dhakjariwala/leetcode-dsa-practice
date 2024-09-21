from typing import *


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        result = 0

        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                # Calculate the number of valid subsequences formed by (nums[left], nums[right])
                # and any element between them
                result = (result + pow(2, right - left, MOD)) % MOD
                left += 1
            else:
                # If the sum is greater than target, move the right pointer to the left
                right -= 1

        return result


sol = Solution()
print(sol.numSubseq([3, 5, 6, 7], 9))
