from typing import *


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1, ans2 = [], []

        for i in range(len(nums1)):
            flag = 0
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    flag = 1
                    break
            if flag != 1:
                ans1.append(nums1[i])
        print(nums1)
        for i in range(len(nums2)):
            flag = 0
            for j in range(len(nums1)):
                if nums2[i] == nums1[j]:
                    flag = 1
                    break
            if flag != 1:
                ans2.append(nums2[i])
        print(nums2)
        return [nums1, nums2]


sol = Solution()
sol.findDifference([1, 2, 3], [2, 4, 6])
