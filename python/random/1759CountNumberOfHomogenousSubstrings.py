class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        result = 0
        count = 1  # Number of consecutive characters

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                # Calculate the number of homogenous substrings for the current group
                result = (result + (count * (count + 1)) // 2) % MOD
                count = 1

        # Calculate for the last group of consecutive characters
        result = (result + (count * (count + 1)) // 2) % MOD

        return result


sol = Solution()
print(sol.countHomogenous("abbcccaa"))
