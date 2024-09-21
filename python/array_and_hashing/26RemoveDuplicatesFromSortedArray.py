from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hash_nums = {}

        for num in nums:
            if num in hash_nums:
                hash_nums[num] = 1 + hash_nums.get(num, 0)
            hash_nums[num] = 1
        print(hash_nums)
        k = 0
        for key, values in hash_nums.items():
            nums[k] = key
            k += 1
        return k