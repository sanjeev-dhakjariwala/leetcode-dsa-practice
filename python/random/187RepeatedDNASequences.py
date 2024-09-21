from typing import *


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()

        for i in range(len(s) - 9):
            current_sequence = s[i : i + 10]

            if current_sequence in seen:
                result.add(current_sequence)
            else:
                seen.add(current_sequence)

        return list(result)


sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
