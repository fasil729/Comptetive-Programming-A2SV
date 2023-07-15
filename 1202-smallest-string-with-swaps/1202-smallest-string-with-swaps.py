class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0 for i in range(size)]

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
        
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
		# 1. Union-Find
        uf = UnionFind(len(s))
        for a, b in pairs:
            uf.union(a, b)

		# 2. Grouping
        group = defaultdict(lambda: ([], []))  
        for i, ch in enumerate(s):
            parent = uf.find(i)
            group[parent][0].append(i)
            group[parent][1].append(ch)

		# 3. Sorting
        res = [''] * len(s)
        for ids, chars in group.values():
            ids.sort()
            chars.sort()
            for ch, i in zip(chars, ids):
                res[i] = ch
                
        return ''.join(res)
