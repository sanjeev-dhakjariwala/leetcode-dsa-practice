class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfNumber(n):
            s = 0

            while n != 0:
                r = n % 10
                s += r * r
                n = n // 10

            return s

        visited = set()

        while n not in visited:
            visited.add(n)
            n = sumOfNumber(n)

            if n == 1:
                return True

        return False

sol = Solution()
print(sol.isHappy(2))