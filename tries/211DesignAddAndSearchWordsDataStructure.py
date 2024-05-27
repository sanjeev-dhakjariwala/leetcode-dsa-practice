class WordDictionary:

    def __init__(self):
        self.word_dict = []

    def addWord(self, word: str) -> None:
        self.word_dict.append(word)

    def searchHelper(self, word, target):
        i = 0
        j = 0
        n1 = len(word)
        n2 = len(target)

        while i < n1 and j < n2:
            if word[i] != '.' and word[i] != target[i]:
                return False
            i += 1
            j += 1
        return True

    def search(self, word: str) -> bool:
        for w in self.word_dict:
            if self.searchHelper(w, word):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
# obj.addWord("mad")
# param_2 = obj.search("pad")
# param_2 = obj.search("bad")
param_2 = obj.search("aa")
# param_2 = obj.search("b..")