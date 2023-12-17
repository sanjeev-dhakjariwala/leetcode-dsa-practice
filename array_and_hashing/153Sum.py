from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        while i < n:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            target = nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] + nums[k] == target:
                    res.append([nums[j], nums[k], target])
                    j += 1
                    k -= 1
                    
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
