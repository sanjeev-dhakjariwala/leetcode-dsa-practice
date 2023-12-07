class Solution:
    def totalMoney(self, n: int) -> int:
        daily = 1
        money = 0
        c = 1
        i = 1
        w = 1
        while i <= n:

            if w > 7:
                daily = daily + 1
                c = daily
                # print(c, end=" ")
                money += c
                c += 1
                i += 1
                w = 2
            else:
                money += c
                # print(c, end="")
                c += 1
                i += 1
                w += 1
        return money


sol = Solution()
print(sol.totalMoney(10))
