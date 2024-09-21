from typing import *
from collections import *


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c = 0
        n = len(word)
        res1 = [-1] * 26
        res2 = [-1] * 26

        for i in range(n):
            if word[i] >= "A" and word[i] <= "Z":
                if res1[ord(word[i]) - 65] == -1:
                    res1[ord(word[i]) - 65] = i
            else:
                res2[ord(word[i]) - 97] = i

        for i in range(len(res2)):
            if res1[i] > res2[i] and res1[i] != -1 and res2[i] != -1:
                c += 1

        return c


sol = Solution()
print(sol.numberOfSpecialChars("ADdadACBC"))
