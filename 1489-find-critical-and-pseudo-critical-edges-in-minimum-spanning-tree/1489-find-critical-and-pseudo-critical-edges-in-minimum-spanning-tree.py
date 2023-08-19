class UnionFind:
    def __init__(self, n):
        self.root = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] == self.rank[root_y]:
                self.root[root_x] = root_y
                self.rank[root_y] += 1
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
    def compenent(self):
        res = 0
        for u,v in self.root.items():
            if u == v:
                res += 1
        return res
    
                


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(edge[0], edge[1], edge[2], ind) for ind, edge in enumerate(edges)] 
        edges.sort(key=lambda x: x[2])
        def mst(edges, critical=None, uncritical=None):
            uf = UnionFind(n)
            res = 0
            if uncritical:
                u, v, w, ind = uncritical
                uf.union(u, v)
                res += w
            for edge in edges:
                u, v, w, ind = edge
                if edge != critical and uf.find(u) != uf.find(v):
                    res += w
                    uf.union(u, v)

            if uf.compenent() != 1:
                    return float("inf")
            return res
        ans = [[], []]
        m_weight = mst(edges)
        for i in range(len(edges)):
            # check critical
            ind = edges[i][3]
            if mst(edges, edges[i]) > m_weight:
                ans[0].append(ind)
            
            # check uncritical
            elif mst(edges, None, edges[i]) == m_weight:
                ans[1].append(ind)
        return ans
            
                    
                    
                
        