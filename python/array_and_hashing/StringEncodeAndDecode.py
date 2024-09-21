from typing import *


class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""

        for s in strs:
            ans += s + "MAKHAN"

        print(ans)

    def decode(self, s: str) -> List[str]:
        ans = s.split("MAKHAN")
        finalAns = []

        for i in range(len(ans) - 1):
            finalAns.append(ans[i])

        return finalAns


sol = Solution()
ans = sol.decode(["neet", "code", "love", "you"])
print(sol.decode())
