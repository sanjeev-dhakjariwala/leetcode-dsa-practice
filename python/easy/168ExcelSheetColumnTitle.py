class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber != 0:
            columnNumber -= 1
            r = columnNumber % 26
            res = chr(65 + r) + res
            columnNumber //= 26
        
        return res


sol = Solution()
print(sol.convertToTitle(701))
# print(sol.convertToTitle(26))
