class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     res = ""
    #
    #     for i in range(len(s)):
    #         for l, r in ((i, i), (i, i + 1)):  # odd and even lengths
    #             while l >= 0 and r < len(s) and s[l] == s[r]:
    #                 if (r - l + 1) > len(res):
    #                     res = s[l: r + 1]
    #                 l -= 1
    #                 r += 1
    #
    #     return res

    def longestPalindrome(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            for j in range(i, len(s)):
                res.append(s[i: j + 1])
        ans = ""
        max_len = float('-inf')
        for r in res:
            if max_len < len(r) and r[::-1] == r:
                max_len = len(r)
                ans = r

        return ans


sol = Solution()
print(sol.longestPalindrome("babad"))
