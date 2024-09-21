from typing import *

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:

        n = len(word)
        ans = 0

        def helper(i, j):
            nonlocal ans
            while i > -1 and j < n:
                s = word[i : j + 1]
                hash_map = Counter(s)
                c = 0
                for key, value in hash_map.items():
                    if value % 2 == 1:
                        c += 1
                if c == 1:
                    ans += 1
                i -= 1
                j += 1
            print(word[i + 1 : j])

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)

        return ans

sol = Solution()
print(sol.wonderfulSubstrings("aabb"))
