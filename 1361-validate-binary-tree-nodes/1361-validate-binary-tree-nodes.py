class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = {}
        uf = UnionFind(n)
        for ind, child in enumerate(leftChild):
            if child == -1:
                continue
            if child in parent:
                return False
            if uf.find(ind) == uf.find(child):
                 return False
            uf.union(ind, child)
            parent[child] = ind
        for ind, child in enumerate(rightChild):
            if child == -1:
                continue
            if child in parent:
                return False
            if uf.find(ind) == uf.find(child):
                 return False
            uf.union(ind, child)
            parent[child] = ind
        return len(parent) == n - 1
        

#         uf = UnionFind(n)
#         for ind, child in enumerate(leftChild):
#             if child == -1:
#                 continue
#             if uf.find(ind) == uf.find(child):
#                 return False
#             uf.union(ind, child)
        
#         for ind, child in enumerate(rightChild):
#             if child == -1:
#                 continue
#             if ind != uf.parent[child] and uf.find(ind) != uf.find(child):
#                 return False
#             uf.union(ind, child)
#         return uf.isOneCompenent()
        

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.parent = [i for i in range(n)]
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        self.parent[y] = x
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += self.rank[rootX]
    
    def isOneCompenent(self):
        comp = 0
        for ind, r in enumerate(self.root):
            if ind == r:
                comp += 1
        return comp == 1
        
        
        
            