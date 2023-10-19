class TrieNode:
    def __init__(self, char=None):
        self.index = -1
        self.children = [None] * 27
        
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.cur = self.root

    def addWord(self, word: str, i) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) % 97
            if not cur.children[ind]:
                cur.children[ind] = TrieNode(c)
            
            cur = cur.children[ind]
            cur.index = max(cur.index, i)
        
    def search(self, word: str):
        cur = self.root
        for c in word:
            ind = ord(c) % 97
            if not cur.children[ind]:
                return -1
            cur = cur.children[ind]
        return cur.index
class WordFilter:

    def __init__(self, words: List[str]):
        self.tr = Trie()
        for ind, word in enumerate(words):
            self.tr.addWord(word + "{" + word, ind)
            for i in range(len(word)):
                entry = word[i + 1:] + "{" + word
                self.tr.addWord(entry, ind)

    def f(self, pref: str, suff: str) -> int:
       
        return self.tr.search(suff + "{" + pref)         


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)