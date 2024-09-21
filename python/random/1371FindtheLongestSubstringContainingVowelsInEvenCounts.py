class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_indices = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        seen = {0: -1}  # Stores the first index where the state is seen

        state = 0  # Represents the XOR of the counts of vowels in the substring
        max_length = 0

        for i, char in enumerate(s):
            if char in vowel_indices:
                state ^= vowel_indices[char]

            if state not in seen:
                seen[state] = i
            else:
                max_length = max(max_length, i - seen[state])

        return max_length
