class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        tr = Trie()
        for word in words:
            tr.insert(word)
        def find_index(char, start):  
            # i am using this for checking if char is exist in s starting from given index
            for i in range(start, n):
                if s[i] == char:
                    return i
            return -1
        count = 0
        def dfs(node, index):
            # print(node.children)
            if index == n:
                return
            nonlocal count
            for i in range(26):
                child = node.children[i]
                if not child:
                    continue
                ind = find_index(child.char, index)
                if ind != -1:
                    
                    count += child.isEndOfWord
                    dfs(child, ind + 1)
        dfs(tr.root, 0)
        return count
                
                
                
    
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
            ind = ord(c) % 26
            if not cur.children[ind]:
                cur.children[ind] = TrieNode(c)
            cur = cur.children[ind]
        cur.isEndOfWord += 1
        
#     def haveOneChild(self, node):
#         children = node.children
#         node = None
#         num = 0
#         for child in children:
#             if child:
#                 num += 1
#                 node = child
#         if num == 1:       
#             return node
#         return None
    
#     def longest_prefix(self):
#         ans = ""
#         cur = self.root
#         while cur and not cur.isEndOfWord and self.haveOneChild(cur)!= None:
#             cur = self.haveOneChild(cur)
#             ans += cur.char
#         return ans

   
        

        