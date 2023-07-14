class UnionFind:
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
            if self.rank[rootX] > self.rank[rootY]:   # optimizing union functtion using rank
                self.root[rootY] = rootX
                
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    def components(self):
        return sum(key == value for key, value in self.root.items())


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        
        for row, col in stones:
            uf.union(row, ~col)  # use ~ operator on col to differtite equal row and col for e.g first row and first column
        
        return len(stones) - uf.components()
        
        