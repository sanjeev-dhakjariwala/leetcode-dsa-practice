class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        i = 1
        ans = ""
        while x > 0 and y > 0:
            if x > 0:
                x -= 1
            else:
                break
            if y > 3:
                y -= 4
            else:
                break
            if i % 2 == 0:
                ans = "Bob"
            else:
                ans = "Alice"
            i += 1
        return ans


x = 5
y = 18
sol = Solution()
print(sol.losingPlayer(x, y))
