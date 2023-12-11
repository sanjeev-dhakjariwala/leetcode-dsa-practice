# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def helper(s):
#             res = []
#             for i in s:
#                 if i != "#":
#                     res.append(i)
#                 elif res:
#                     res.pop()
#             return res
#
#         return helper(s) == helper(t)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1, stk2 = [], []

        for i in s:
            if len(stk1) > 0 and i == '#':
                stk1.pop()
            else:
                stk1.append(i)
        for i in t:
            if len(stk2) > 0 and i == '#':
                stk2.pop()
            else:
                stk2.append(i)
        print(stk1, stk2)
        return stk1 == stk2


sol = Solution()

print(sol.backspaceCompare("y#fo##f", "y#f#o##f"))
