class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        res = []
        i = 0
        left = False
        right = True
        while k > -1:
            if i > 0 and i < n - 1 and right:
                res.append(i)
                i += 1
                k -= 1
            elif i > 0 and i < n - 1 and left:
                res.append(i)
                i -= 1
                k -= 1
            else:
                res.append(i)
                if i == n - 1:
                    i -= 1
                    k -= 1
                    left = True
                    right = False
                elif i == 0:
                    left = False
                    right = True
                    i += 1
                    k -= 1
        print(res)
        return res[-1]

sol = Solution()
print(sol.numberOfChild(3, 5))