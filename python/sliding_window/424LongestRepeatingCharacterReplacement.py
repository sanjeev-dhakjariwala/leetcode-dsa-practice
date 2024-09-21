from typing import *


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_count = 0
        count = {}
        start = 0

        for end in range(len(s)):
            count[s[end]] = 1 + count.get(s[end], 0)
            max_count = max(max_count, count[s[end]])

            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)

        return max_length


sol = Solution()
print(sol.characterReplacement("ABAB", 2))
