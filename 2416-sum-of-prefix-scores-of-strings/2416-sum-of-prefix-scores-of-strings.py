class TrieNode:
    def __init__(self, char=None):
        self.count = 0
        self.children = [None] * 27
        
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) % 97
            if not cur.children[ind]:
                cur.children[ind] = TrieNode(c)
            
            cur = cur.children[ind]
            cur.count += 1
        
    def scoreSum(self, word: str):
        cur = self.root
        ans = 0
        for c in word:
            ind = ord(c) % 97
            cur = cur.children[ind]
            ans += cur.count
        return ans
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tr = Trie()
        for word in words:
            tr.addWord(word)
        ans = []
        for word in words:
            res = tr.scoreSum(word)
            ans.append(res)
        return ans

        
