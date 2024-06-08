from typing import *
from collections import *

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def freq_counter(word):
            freq_counter = defaultdict(int)
            for w in word:
                freq_counter[w] += 1
            return freq_counter
        
        base_map = freq_counter(words[0])
        for i in (1, len(words)):
            curr_map = freq_counter(words[i])

            for key, value in base_map.items():
                if key in curr_map:
                    base_map[key] = min(base_map[key], curr_map[key])
                else:
                    base_map[key] = 0
        
        res = []
        for key, value in base_map.items():
            if value > 0:
                res.extend([key] * value)
        
        return res

sol = Solution()
print(sol.commonChars(["bella","label","roller"]))