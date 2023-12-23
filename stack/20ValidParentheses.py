class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stk.append(i)
            elif len(stk) > 0:
                ele = stk.pop()
                if (
                    (ele == "(" and i == ")")
                    or (ele == "{" and i == "}")
                    or (ele == "[" and i == "]")
                ):
                    continue
                else:
                    return False
            else:
                return False
            

            return len(stk) == 0




        # stk = []

        # for i in s:
        #     if i == '(' or i == '[' or i == '{':
        #         stk.append(i)
        #     else:
        #         if len(stk) > 0:
        #             ele = stk.pop()
        #             if ((ele == '(' and i == ')') or (ele == '[' and i == ']') or (ele == '{' and i == '}') ):
        #                 continue
        #             else:
        #                 return False
        #         else:
        #             return False
        # return len(stk) == 0


sol = Solution()
print(sol.isValid("(){}}{"))
