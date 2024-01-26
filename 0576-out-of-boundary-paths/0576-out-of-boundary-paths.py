class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        @cache
        def dp(maxMove, row, col):
            # top down dp approach
            if not inbound(row, col):
                return 1
            
            if maxMove == 0:
                return 0
            
            ans = 0
            
            direc = [[0, -1], [-1, 0,], [1, 0], [0, 1]]
                               
            for r, c in direc:
                nr = row + r
                nc = col + c
                ans += dp(maxMove - 1, nr, nc)
                
            return ans % MOD
        
        return dp(maxMove, startRow, startColumn) 
                     
                               
        