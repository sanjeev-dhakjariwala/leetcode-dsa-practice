from typing import *

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_map = {0: 1}
        curr_sum = 0
        c = 0

        for i,num in enumerate(nums):
            curr_sum += num
            rem = curr_sum % k

            if rem in hash_map:
                c += hash_map[rem]
                hash_map[rem] += 1
            else:
                hash_map[rem] = 1

        return c

sol = Solution()
nums = [4,5,0,-2,-3,1]
print(sol.subarraysDivByK(nums, 5))