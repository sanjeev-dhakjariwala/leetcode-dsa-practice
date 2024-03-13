from typing import *
from collections import *


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Convert wordList to a set for faster lookup
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque(
            [(beginWord, 1)]
        )  # Queue to store words and their corresponding level
        visited = set()  # Set to keep track of visited words

        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level

            # Generate all possible transformations of the current word by changing one letter at a time
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nextWord = word[:i] + c + word[i + 1 :]
                    if nextWord in wordSet and nextWord not in visited:
                        visited.add(nextWord)
                        queue.append((nextWord, level + 1))

        return 0


sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
