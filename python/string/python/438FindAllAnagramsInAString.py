from typing import *


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        window_size = len(p)
        p_counter = {}
        current_counter = {}

        for i in p:
            p_counter[i] = 1 + p_counter.get(i, 0)

        # Initialize current_counter with the character counts of the first window
        for i in s[:window_size]:
            current_counter[i] = 1 + current_counter.get(i, 0)

        for i in range(len(s) - window_size + 1):
            if current_counter == p_counter:
                result.append(i)

            # Update the current window by removing the leftmost character and adding the rightmost character
            if i + window_size < len(s):
                current_counter[s[i]] -= 1
                if current_counter[s[i]] == 0:
                    del current_counter[s[i]]
                current_counter[s[i + window_size]] = 1 + current_counter.get(
                    s[i + window_size], 0
                )

        return result


sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
