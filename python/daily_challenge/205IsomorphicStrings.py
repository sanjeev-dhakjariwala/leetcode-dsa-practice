class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_map = {}
        for i in range(0, len(s)):
            if t[i] not in hash_map:
                tmp_values = hash_map.values()
                if s[i] in tmp_values:
                    return False
                hash_map[t[i]] = s[i]
            elif hash_map[t[i]] != s[i]:
                return False
        return True


sol = Solution()
print(sol.isIsomorphic("foo", "bar"))
