class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        i = 0
        j = 0
        ans = ""
        while i < n1 and j < n2:
            ans += word1[i] + word2[j]
            i += 1
            j += 1
        if i < n1:
            ans += word1[i:n1]
        if j < n2:
            ans += word2[j:n2]
        return ans


sol = Solution()
word1 = "ab"
word2 = "pqrs"
print(sol.mergeAlternately(word1, word2))
