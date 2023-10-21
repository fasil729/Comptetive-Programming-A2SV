class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.prev = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        diff = self.prev[key]
        self.prev[key] = val
        val -= diff
        for c in key:
            ind = ord(c) % 97
            if not cur.children[ind]:
                cur.children[ind] = TrieNode(c)
            cur = cur.children[ind]
            cur.val += val
        cur.isEndOfWord = True

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            ind = ord(c) % 97
            if not cur.children[ind]:
                return 0
            cur = cur.children[ind]
        return cur.val
           

class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.children = [None] * 26
        self.isEndOfWord = False
        self.val = 0



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)