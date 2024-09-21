from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash1 = Counter(ransomNote)
        hash2 = Counter(magazine)
        print(hash1)
        print(hash2)
        c = 0
        for key, item in hash2.items():
            if hash1[key] <= item:
                c += hash1[key]
        if c == 0:
            return False
        print(c)
        return True if c == len(ransomNote) else False


sol = Solution()
print(sol.canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))
