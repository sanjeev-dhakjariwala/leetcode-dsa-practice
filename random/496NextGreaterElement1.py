from typing import *


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        # Iterate through nums2 to find the next greater element for each element
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        # For elements in nums1, get their next greater element from the dictionary
        ans = [next_greater.get(num, -1) for num in nums1]
        return ans


sol = Solution()
print(sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
