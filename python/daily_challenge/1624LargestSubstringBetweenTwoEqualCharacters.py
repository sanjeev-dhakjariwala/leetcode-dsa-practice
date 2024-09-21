class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n = len(s)
        max_len = -1
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    max_len = max(max_len, ((j - 1) - (i + 1) + 1))

        return max_len
