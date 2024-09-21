from typing import *
from collections import Counter


# ChatGPT
# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         len_s1, len_s2 = len(s1), len(s2)
#
#         if len_s1 > len_s2:
#             return False
#
#         counter_s1 = Counter(s1)
#         counter_window = Counter(s2[:len_s1])
#
#         for i in range(len_s2 - len_s1 + 1):
#             if counter_window == counter_s1:
#                 return True
#
#             if i + len_s1 < len_s2:
#                 counter_window[s2[i]] -= 1
#                 if counter_window[s2[i]] == 0:
#                     del counter_window[s2[i]]
#                 counter_window[s2[i + len_s1]] += 1
#
#         return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26


sol = Solution()
print(sol.checkInclusion("ab", "eidbaooo"))
