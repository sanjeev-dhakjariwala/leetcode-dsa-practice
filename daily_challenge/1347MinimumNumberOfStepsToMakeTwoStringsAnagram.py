class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if len(s) != len(t):
            return -1  # Invalid input, strings must be of the same length

        # Initialize frequency dictionaries for both strings
        freq_s = {}
        freq_t = {}

        # Count the frequency of each character in string s
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        # Count the frequency of each character in string t
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Calculate the difference in frequencies
        diff = 0
        for char in set(freq_s.keys()).union(set(freq_t.keys())):
            diff += abs(freq_s.get(char, 0) - freq_t.get(char, 0))

        return (
            diff // 2
        )  # Divide by 2 because each step involves changing one character, and we counted each difference twice


sol = Solution()
print(sol.minSteps("leetcode", "practice"))
