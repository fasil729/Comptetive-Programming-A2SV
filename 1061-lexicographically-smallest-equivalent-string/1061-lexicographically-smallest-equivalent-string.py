class UnionFind:     # union find template to use every where with amortized O(1) time and O(n) space complexity
    def __init__(self):
        self.root = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        self.check(x)         # check if the x exist in self root 
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) # path compression
        return self.root[x]
    
    def check(self, node):
        if not node in self.root:      # add node:node key to root dict if node does not exist in root
            self.root[node] = node
        return
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if rootX < rootY:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
            
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        res = ""
        for char in baseStr:
            res += uf.find(char)
        return res
        