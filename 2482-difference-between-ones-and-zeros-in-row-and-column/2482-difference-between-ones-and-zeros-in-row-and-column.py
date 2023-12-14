class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid[0])
        n = len(grid)
        row_count = [0] * n
        col_count = [0] * m
        diff = [[0] * m for i in range(n)]
        
        
        
        for row in range(n):
            for col in range(m):
                if grid[row][col]:
                    row_count[row] += 1
                    col_count[col] += 1
                else:
                    row_count[row] -= 1
                    col_count[col] -= 1
                    
        
        for row in range(n):
            for col in range(m):
                diff[row][col] = row_count[row] + col_count[col]
                
        return diff
        
        