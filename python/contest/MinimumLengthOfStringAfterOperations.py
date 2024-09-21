class Solution:
    def minimumLength(self, s: str) -> int:
        def findChar(char, i, dir):
            while i < len(s) if dir == "right" else i > -1:
                if char == s[i]:
                    return i
                if dir == "left":
                    i -= 1
                else:
                    i += 1
            return -1

        n = len(s)
        if s == 2:
            return n
        i = 1
        while i < n:
            left = findChar(s[i], i - 1, "left")
            right = findChar(s[i], i + 1, "right")
            if left != -1 and right != -1:
                s = s[0:left] + "0" + s[left + 1 : right] + "0" + s[right + 1 : n]
            print(s)
            i += 1
        c = 0
        for char in s:
            if char != "0":
                c += 1

        return c


sol = Solution()
# s = "abaacbcbb"
# s = "aa"
s = "abcabc"
print(sol.minimumLength(s))
