class UnionFind:
    def __init__(self, account):
        self.root = {acc:acc for acc in account}
        self.rank =  {acc: 0 for acc in account}

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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ans = defaultdict(list)
        
        emails = []
        for account in accounts:
            name = account[0]
            for ema in account[1:]:
                emails.append((ema, name))
        uf = UnionFind(emails)
        for account in accounts:
            name = account[0]
            email = account[1]
            for ema in account[1:]:
                uf.union((email, name), (ema, name))
        for email, name in sorted(uf.root.keys()):
            ans[uf.find((email, name))].append(email)
        res = []
        for email, name in ans:
            arr = ans[(email, name)]
            arr.insert(0, name)
            res.append(arr)
        return res
            
            
            
            
        
        
        
        