class UnionFind:
    def __init__(self, size):
        self.root = {i:i for i in range(size)}
        self.rank = {i:1 for i in range(size)}
        
    def find(self, x):
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[x] > self.rank[y]:
                self.root[rootY] = rootX
                self.rank[x] += self.rank[y]
            else:
                self.root[rootX] = rootY
                self.rank[rootX] += self.rank[rootY]





class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # Approach the question using UNIONFIND method
        n = len(isConnected)
        dsu = UnionFind(n)
        
        ans = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and dsu.find(i) != dsu.find(j):
                    ans -= 1
                    dsu.union(i, j)
        return ans
            

        