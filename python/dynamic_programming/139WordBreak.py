from typing import *


class Solution:
    def wordBreakRecursive(self, s: str, wordDict: List[str]) -> bool:
        def canSegment(s: str, wordDict: List[str]) -> bool:
            if not s:
                return True
            for word in wordDict:
                if s.startswith(word):
                    if canSegment(s[len(word) :], wordDict):
                        return True
            return False

        return canSegment(s, wordDict)
    
    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        # Create a set for faster lookup
        wordSet = set(wordDict)
            
        # Initialize a list to store whether the substring from index 0 to i can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True
            
        for i in range(1, len(s) + 1):
            for j in range(i):
                    # Check if the substring from index j to i exists in the wordSet and
                    # if the substring from index 0 to j can be segmented
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
            
        return dp[len(s)]

sol = Solution()
# print(sol.wordBreakRecursive("leetcode", ["leet", "code"]))
print(sol.wordBreakDP("leetcode", ["leet", "code"]))