from typing import *

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for word in words[0]:
            c = 0
            for i in range(1, len(words)):
                if word in words[i]:
                    res.append(word)
                    c += 1
            if c == len(words) - 1:
                res.append(word)
                
        return res

sol = Solution()
words = ["bella","label","roller"]
sol.commonChars(words)