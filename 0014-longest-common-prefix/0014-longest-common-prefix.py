class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        if "" in v:
            return ""
        t = Trie()
        for word in v:
            t.insert(word)
        return t.longest_prefix()
            
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) % 26
            if not cur.children[ind]:
                cur.children[ind] = TrieNode(c)
            cur = cur.children[ind]
        cur.isEndOfWord = True
        
    def haveOneChild(self, node):
        children = node.children
        node = None
        num = 0
        for child in children:
            if child:
                num += 1
                node = child
        if num == 1:       
            return node
        return None
    
    def longest_prefix(self):
        ans = ""
        cur = self.root
        while cur and not cur.isEndOfWord and self.haveOneChild(cur)!= None:
            cur = self.haveOneChild(cur)
            ans += cur.char
        return ans

   
        
class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = [None] * 26
        self.isEndOfWord = False
        