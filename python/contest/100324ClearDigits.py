class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        res = []
        for i in range(0, n):
            if ord(s[i]) >= 48 and ord(s[i]) <= 57 and i > 0:
                res.pop()
            else:
                res.append(s[i])
        
        return "".join(res)

sol = Solution()
s = "cb34"
print(sol.clearDigits(s))