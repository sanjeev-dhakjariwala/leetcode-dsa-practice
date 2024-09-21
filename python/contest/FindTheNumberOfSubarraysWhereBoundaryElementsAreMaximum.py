from typing import *
from collections import *


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:

        def helper():
            res = []
            n = len(nums)
            for i in range(n):
                for j in range(i, n):
                    res.append(nums[i : j + 1])

            print(res)

        # helper()
        hash_map = defaultdict(int)
        hash_map_index = defaultdict(list)
        n = len(nums)
        special = 0
        for i in range(n):
            if hash_map[nums[i]]:
                if abs(hash_map_index[nums[i]][-1] - i) == 1:
                    hash_map[nums[i]] = 1 + hash_map.get(nums[i], 0)
                    hash_map_index[nums[i]].append(i)
                else:
                    special += 1
            else:
                hash_map[nums[i]] = 1 + hash_map.get(nums[i], 0)
                hash_map_index[nums[i]].append(i)

        print(hash_map)
        ans = 0
        for key, val in hash_map.items():
            if val == 1:
                ans += 1
            else:
                ans += (val * (val + 1)) // 2
        return ans + special


sol = Solution()
print(sol.numberOfSubarrays([6, 26, 6, 3, 6, 6]))
# print(sol.numberOfSubarrays([3, 3, 3]))
