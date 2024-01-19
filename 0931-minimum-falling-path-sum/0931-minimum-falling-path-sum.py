class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # top down dp approach
        n = len(matrix)
        m = len(matrix[0])
        direc = [[1, -1], [1, 0], [1, 1]]
        
        @cache
        def dp(row, col):
            if row == n:
                return 0
            if not ( 0 <= col < m ):
                return inf
            
            ans = inf
            for r, c in direc:
                n_r, n_c = row + r, col + c
                
                ans = min(ans, dp(n_r, n_c))
            
            return ans + matrix[row][col]
        
        
        ans = inf
        for ind in range(m):
            ans = min(ans, dp(0, ind))
        
        return ans
            
            
         
        