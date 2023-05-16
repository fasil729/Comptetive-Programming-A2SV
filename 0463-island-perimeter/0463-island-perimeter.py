class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(row, col):
            if (row, col) in visited:
                return 0
            if not (0 <= row < m and 0 <= col < n):
                return 1
            if not grid[row][col]:
                return 1
            
            visited.add((row, col))   
            res = 0
            res += dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
            return res
        
        for row, arr in  enumerate(grid):
            for col, num in enumerate(arr):
                if num:
                    return dfs(row, col)
                    
            
                
                
        