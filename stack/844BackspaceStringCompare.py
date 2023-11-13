class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def helper(s):
            res = []
            for i in s:
                if i != "#":
                    res.append(i)
                elif res:
                    res.pop()
            return res

        return helper(s) == helper(t)


sol = Solution()
print(sol.backspaceCompare("y#fo##f", "y#f#o##f"))
