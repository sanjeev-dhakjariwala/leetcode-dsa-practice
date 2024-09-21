class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_set = {}
        n = len(s)
        for i in range(n):
            hash_set[s[i]] = 1 + hash_set.get(s[i], 0)
        print(hash_set)
        for i in range(n):
            if s[i] in hash_set and hash_set[s[i]] == 1:
                return i

        return -1


sol = Solution()
print(sol.firstUniqChar("leetcode"))
