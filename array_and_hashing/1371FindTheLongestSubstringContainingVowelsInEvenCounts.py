class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        # Mapping of XOR value to the index where it was first encountered
        xor_to_index = {0: -1}
        xor = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                # Toggle the corresponding bit in XOR if the vowel is encountered
                xor ^= (ord(char) - ord("a") + 1)

            # Check if the current XOR value has been encountered before
            if xor in xor_to_index:
                max_length = max(max_length, i - xor_to_index[xor])
            else:
                xor_to_index[xor] = i

        return max_length
        # c_m = [
        #     1,
        #     0,
        #     0,
        #     0,
        #     2,
        #     0,
        #     0,
        #     0,
        #     4,
        #     0,
        #     0,
        #     0,
        #     0,
        #     0,
        #     8,
        #     0,
        #     0,
        #     0,
        #     0,
        #     0,
        #     16,
        #     0,
        #     0,
        #     0,
        #     0,
        #     0,
        # ]
        # mask = 0
        # res = 0
        # m = [-1] * 32

        # for i in range(len(s)):
        #     mask ^= c_m[ord(s[i]) - ord("a")]
        #     if mask != 0 and m[mask] == -1:
        #         m[mask] = i
        #     res = max(res, i - m[mask])

        # return res


sol = Solution()
print(sol.findTheLongestSubstring("eleetminicoworoep"))
