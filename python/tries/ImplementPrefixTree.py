from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(str)
        self.next = TrieNode
        self.is_word = False
        
class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children.add(w)
                node = TrieNode()
                curr.next = node
            curr = curr.children[w]
        curr.is_word = True

    def search(self, word: str) -> bool:
        return True

    def startsWith(self, prefix: str) -> bool:
        return True

sol = PrefixTree()
sol.insert("car")
sol.insert("cart")