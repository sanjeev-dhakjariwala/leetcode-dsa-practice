from typing import *


class Solution:
    def countSubarrays(self, arr: List[int], k: int) -> int:
        subarrays = []
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarray = arr[i:j + 1]
                subarrays.append(subarray)
        print(subarrays)
        max_ele = max(arr)
        print(max_ele)
        for sub in subarrays:
            c = 0
            for i in sub:
                if max_ele == i:
                    c += 1
            if c >= k:
                ans += 1

        return ans


sol = Solution()
print(sol.countSubarrays([28, 5, 58, 91, 24, 91, 53, 9, 48, 85, 16, 70, 91, 91, 47, 91, 61, 4, 54, 61, 49], 1))
