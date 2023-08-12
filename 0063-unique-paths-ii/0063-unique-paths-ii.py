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
       
        