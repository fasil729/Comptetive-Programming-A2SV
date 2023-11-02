class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        def dfs(row, col):
            grid[row][col] = 0
            
            direc = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            
            for r, c in direc:
                n_c = col + c
                n_r = row + r
                if inbound(n_r, n_c) and grid[n_r][n_c] == 1:
                    dfs(n_r, n_c)
                
        
        boundary = [(0, col) for col in range(m) if grid[0][col] == 1]
        boundary += [(row, 0) for row in range(n) if grid[row][0] == 1]
        boundary += [(row, m - 1) for row in range(n) if grid[row][m - 1] == 1]
        boundary += [(n - 1, col) for col in range(m) if grid[n - 1][col] == 1]
        
        for row, col in boundary:
            dfs(row, col)
        ans = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    ans += 1
        return ans
        