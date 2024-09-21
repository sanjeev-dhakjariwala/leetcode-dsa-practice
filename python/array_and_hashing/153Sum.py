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
            j = i + 1
            k = n - 1
            while j < k:
                threeSum = nums[j] + nums[k] + nums[i]
                if threeSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
        return res


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
