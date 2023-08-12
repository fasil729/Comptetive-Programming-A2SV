class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        # TOP DOWN DP APPROACH
        @cache
        def dp(row, col):
            if row == (n - 1) and col == (m - 1) and not obstacleGrid[row][col]:
                return 1
            if row == n or col == m:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            
            return dp(row + 1, col) + dp(row, col + 1)
        
        return dp(0, 0)
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def get(row, col):
            if row < n and col < m:
                return dp[(row, col)]
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        if obstacleGrid[n - 1][m - 1] == 1:
            return 0
        # bottom up approach
        dp = {(n - 1, m - 1): 1}
        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    dp[(row, col)] = 0
                elif row == n - 1 and col == m - 1:
                    continue
                else:
                    dp[(row, col)] = get(row + 1, col) + get(row, col + 1)
        return dp[(0, 0)]
   
                    
    
       
        