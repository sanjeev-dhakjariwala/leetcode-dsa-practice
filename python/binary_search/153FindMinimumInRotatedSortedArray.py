from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]


sol = Solution()
nums = [3, 4, 5, 6, 1, 2]
print(sol.findMin(nums))
