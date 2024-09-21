class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1  # Initialize max_power to 1 to handle single-character strings
        current_power = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_power += 1
            else:
                max_power = max(max_power, current_power)
                current_power = 1

        # Update max_power after the loop for the last group of consecutive characters
        max_power = max(max_power, current_power)

        return max_power


sol = Solution()
print(sol.maxPower("leetcode"))
