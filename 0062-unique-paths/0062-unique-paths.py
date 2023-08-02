class Solution:
    def uniquePaths2(self, m: int, n: int) -> int:
        
        # top_down dp approach
        @lru_cache
        def dp(row, col):
            if row == m - 1 and col == n - 1:
                return 1
            if row == m  or col == n:
                return 0
            return dp(row + 1, col) + dp(row, col + 1)
        
        return dp(0, 0)
    
    def uniquePaths(self, m: int, n: int) -> int:
        
        # bottom-up dp approach  
        dp = [[0] * n for i in range(m)]
        
        def get(row, col):
            if 0 <= row < m and 0 <= col < n:
                return dp[row][col]
            return 0
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m -1 and j == n - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = get(i + 1, j) + get(i, j + 1)
        
        return dp[0][0]
                
    
    