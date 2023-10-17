class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = [None] * 26
        self.isEndOfWord = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            ind = ord(c) % 97
            if not cur.children[ind]:
                cur.children[ind] = TrieNode(c)
            cur = cur.children[ind]
        cur.isEndOfWord += 1  
class Solution:
    def longestWord(self, words: List[str]) -> str:
        tr = Trie()
        for word in words:
            tr.insert(word)
        longest_ans = ""
        def dfs(node, ans):
            nonlocal longest_ans
            for i in range(26):
                child = node.children[i]
                if child and child.isEndOfWord:
                    if len(longest_ans) < len(ans) + 1:
                        
                        longest_ans = ans + child.char
                    dfs(child, ans + child.char)
        dfs(tr.root, "")
        return longest_ans