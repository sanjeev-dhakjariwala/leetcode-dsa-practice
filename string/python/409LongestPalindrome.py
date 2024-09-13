class Solution:
    def longestPalindrome(self, s: str) -> int:
        i, j = 0, len(s) - 1
        max_len = -1
        while i < j:
            if s[i : j + 1] == s[i : j + 1 : -1]:
                max_len = max(max_len, j - i)
            i += 1
            j -= 1
        return max_len


sol = Solution()
print(sol.longestPalindrome("abccccdd"))
