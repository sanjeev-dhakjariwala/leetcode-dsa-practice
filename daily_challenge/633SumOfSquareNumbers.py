class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 1
        high = int(c ** 0.5)

        while low <= high:
            temp = (low ** 2) + (high ** 2)
            if temp == c:
                return True
            elif temp < c:
                low += 1
            else:
                high -= 1
        return False

sol = Solution()
print(sol.judgeSquareSum(4))