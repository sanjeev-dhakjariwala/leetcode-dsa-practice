class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        if (red == 1 and blue == 1) or (blue == 1 and red == 1):
            return 1
        if (red + blue) % 2 == 0:
            if red < blue:
                first = blue
                second = red
            else:
                first = red
                second = blue
        else:
            if red < blue:
                first = red
                second = blue
            else:
                first = blue
                second = red
        i = 1
        j = 2
        k = 0
        c = 0
        last = 0
        while True:
            if k % 2 == 0 and first > 0 and first >= last:
                first -= i
                last = i
                i += 2
                c += 1
            elif k % 2 == 1 and second > 0 and second >= last:
                second -= j
                last = second
                last = j
                j += 2
                c += 1
            else:
                break
            k += 1
        return c


sol = Solution()
print(sol.maxHeightOfTriangle(10, 10))
