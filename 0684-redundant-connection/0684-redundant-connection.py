class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x]) # path compression
        return self.root[x]
       
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:   # optimizing union functtion using rank
                self.root[rootY] = rootX
                
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # approach the question using union find
        n = len(edges)
        uf = UnionFind(n)
        
        for u, v in edges:
            if uf.find(u - 1) == uf.find(v - 1):
                ans = [u, v]
            uf.union(u - 1, v - 1)
        return ans
        
        
        