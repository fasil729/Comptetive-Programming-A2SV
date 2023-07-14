class UnionFind:     # union find template to use every where with amorized O(1) time and O(n) space complexity
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
            if self.rank[rootX] > self.rank[rootY]:   # optimizing union function using rank
                self.root[rootY] = rootX
                
            elif self.rank[rootX] > self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def check(self, row, col):
        return 0 <= col < self.m and 0 <= row < self.n 
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.n = len(grid)
        self.m = len(grid[0])
        n = len(grid)
        m = len(grid[0])
        uf = UnionFind()
        for row in range(n):
            for col in range(m):
                st = grid[row][col]
                if st == 1:
                    if self.check(row, col + 1) and grid[row][col + 1] in {1, 3, 5}:
                        uf.union((row, col), (row, col + 1))
                elif st == 2:
                    if self.check(row + 1, col) and grid[row+ 1][col] in {2, 5, 6}:
                        uf.union((row, col), (row + 1, col))
                elif st == 3:
                    if self.check(row + 1, col) and grid[row+ 1][col] in {2, 5, 6}:
                        uf.union((row, col), (row + 1, col))
                elif st == 4:
                    if self.check(row + 1, col) and grid[row+ 1][col] in {2, 5, 6}:
                        uf.union((row, col), (row + 1, col))
                    if self.check(row, col + 1) and grid[row][col + 1] in {1, 3, 5}:
                        uf.union((row, col), (row, col + 1))
                elif st == 6:
                    if self.check(row, col + 1) and grid[row][col + 1] in {1, 3, 5}:
                        uf.union((row, col), (row, col + 1))
        # print(uf.find((0, 0)), uf.find((n - 1, m - 1))
        #     ) 
        # print(uf.root)
        return uf.find((0, 0)) == uf.find((n - 1, m - 1))
            
                    
                    
                
        