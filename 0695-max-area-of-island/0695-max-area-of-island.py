class UnionFind:
    def __init__(self, n, m, grid):
        self.root = {(i, j):(i, j) for i in range(n) for j in range(m)}
        self.rank =  {(i, j):1 if grid[i][j] else 0 for i in range(n) for j in range(m)}

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
                self.rank[rootX] += self.rank[rootY]
        
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += self.rank[rootX]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        uf = UnionFind(n, m, grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i < n - 1 and grid[i + 1][j]:
                        uf.union((i, j), (i + 1, j))
                    if j < m - 1 and grid[i ][j + 1]:
                        uf.union((i, j), (i , j + 1))
        ans = 0
        for val in uf.rank.values():
            ans = max(ans, val)
        return ans
            
        
                










class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        ans = 0
        def dfs(row, col):
            if not(0 <= row < m and 0 <= col < n) or not grid[row][col]:
                return 0
            if (row, col) in visited:
                return 0
            visited.add((row, col))
            res = 1
            res += dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
            return res
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, dfs(i, j))
        return ans
            
        
            
                
        
        