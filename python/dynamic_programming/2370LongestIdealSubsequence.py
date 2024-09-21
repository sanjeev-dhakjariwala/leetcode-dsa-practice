class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        res = []
        n = len(s)
        max_len = float("-inf")

        def check(temp):
            nonlocal max_len
            i = 0
            c = 0
            n = len(temp)

            while i < n - 1:
                if abs(ord(temp[i]) - ord(temp[i + 1])) > k:
                    break
                i += 1

            max_len = max(max_len, i + 1)

        def helper(i, p):
            if i >= n:
                res.append(p)
                return

            helper(i + 1, p + s[i])
            helper(i + 1, p)

        helper(0, "")
        print(res)

        for r in res:
            check(r)

        return max_len


sol = Solution()
print(sol.longestIdealString("acfgbd", 2))
