from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """def helper(temp, depth):
        if len(temp) == len(nums):
            res.append(temp[:])
            return
        for i in range(0, len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            print(f"{'  ' * depth}Current temp: {temp}")
            helper(temp, depth + 1)
            temp.pop()
            print(f"{'  ' * depth}Temp after popping: {temp}")"""

        def helper(temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for num in nums:
                if num in temp:
                    continue
                temp.append(num)
                helper(temp)
                temp.pop()

        res = []
        helper([])  # Start with depth 0
        return res


# Example usage:
solution = Solution()
nums = [1, 2, 3]
print(solution.permute(nums))
