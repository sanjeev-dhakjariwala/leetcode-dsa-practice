from typing import *

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        a = [1] * n
        
        while k > 0:
            for i in range(1, n):
                a[i] = (a[i - 1] + a[i]) % ((10 ** 9) + 7)
            k -= 1
        
        return a[n - 1]

sol = Solution()
print(sol.valueAfterKSeconds(5, 1000))