from typing import *
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums, low, high, target):
            if low > high:
                return -1
            mid = low + (high - low) // 2
            print(mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return helper(nums, low, mid - 1, target)
            else:
                return helper(nums, mid + 1, high, target)

        ans = helper(nums, 0, len(nums) - 1, target)
        return ans
