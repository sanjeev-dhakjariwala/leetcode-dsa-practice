from typing import *
class Solution:
    def lengthOfLIS(self, nums):
        memo = {}
        def recursive_helper(prev_index, current_index):
            if current_index == len(nums):
                return 0

            if (prev_index, current_index) in memo:
                return memo[(prev_index, current_index)]

            include_current = 0
            if prev_index == -1 or nums[current_index] > nums[prev_index]:
                include_current = 1 + recursive_helper(current_index, current_index + 1)

            exclude_current = recursive_helper(prev_index, current_index + 1)

            result = max(include_current, exclude_current)
            memo[(prev_index, current_index)] = result
            return result

        return recursive_helper(-1, 0)
    
    
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     LIS = [1] * len(nums)

    #     for i in range(len(nums) - 1, -1, -1):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] < nums[j]:
    #                 LIS[i] = max(LIS[i], 1 + LIS[j])
    #     return max(LIS)


sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
