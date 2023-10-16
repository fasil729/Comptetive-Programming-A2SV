class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) % 26
            if not cur.children[ind]:
                cur.children[ind] = TrieNode()
            cur = cur.children[ind]
        cur.isEndOfWord = True
        
        
    
    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            ind = ord(c) % 26
            if not cur.children[ind]:
                return False
            cur = cur.children[ind]
        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            ind = ord(c) % 26
            if not cur.children[ind]:
                return False
            cur = cur.children[ind]
        return True
        
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)