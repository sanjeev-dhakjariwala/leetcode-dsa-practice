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
                xor ^= 1 << (ord(char) - ord("a"))

            # Check if the current XOR value has been encountered before
            if xor in xor_to_index:
                max_length = max(max_length, i - xor_to_index[xor])
            else:
                xor_to_index[xor] = i

        return max_length


sol = Solution()
print(sol.findTheLongestSubstring("ixzhsdka"))
