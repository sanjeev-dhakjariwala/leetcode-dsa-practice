from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = Counter(words)

        # Sort the words by frequency and lexicographical order
        sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))

        # Return the first k words
        return sorted_words[:k]


sol = Solution()
print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
