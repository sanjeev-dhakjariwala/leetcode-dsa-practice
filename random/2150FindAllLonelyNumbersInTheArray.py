from typing import *


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        ans = []
        hash_map = {}
        for num in nums:
            if num in hash_map:
                print(hash_map.get(num, 0), end=" ")
                hash_map[num] = 1 + hash_map.get(num, 0)
            hash_map[num] = 1
        print(hash_map)
        for num in nums:
            if (
                num - 1 not in hash_map
                and num + 1 not in hash_map
                and hash_map[num] == 1
            ):
                ans.append(num)
        return ans


sol = Solution()
print(sol.findLonely([1, 3, 5, 3]))
