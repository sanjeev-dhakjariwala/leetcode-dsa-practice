from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = self.binarySearch(nums, 0, len(nums) - 1, True, target)
        right = self.binarySearch(nums, 0, len(nums) - 1, False, target)
        return [left, right]

    def binarySearch(self, nums, low, high, part, target):
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                ans = mid
                if part:
                    high = mid - 1
                else:
                    low = mid + 1

        return ans

sol = Solution()
nums = [5, 7, 7, 8, 8, 10]
print(sol.searchRange(nums, 8))