class Solution:
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
            
        
            
                
        
        