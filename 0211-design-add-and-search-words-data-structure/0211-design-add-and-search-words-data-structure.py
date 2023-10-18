class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = [None] * 26
        self.isEndOfWord = 0
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.cur = self.root

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) % 97
            if not cur.children[ind]:
                cur.children[ind] = TrieNode(c)
            cur = cur.children[ind]
        cur.isEndOfWord += 1  

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        n = len(word)
        while stack:
            cur, ind = stack.pop()
            c = word[ind]
            if c == "." and ind == n - 1:
                for child in cur.children:
                    if child and child.isEndOfWord:
                        return True
                continue
                
            if c == ".":
                for child in cur.children:
                    if child:
                        stack.append((child, ind + 1))
                continue
            index = ord(c) % 97
            child = cur.children[index]
            if child and ind == n - 1:
                if child.isEndOfWord:
                    return True
            elif child:
                stack.append((child, ind + 1))
        return False
            
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)