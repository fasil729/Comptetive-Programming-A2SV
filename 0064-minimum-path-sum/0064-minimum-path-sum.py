class Solution:
    def minPathSum(self,grid:List[List[int]])->int:
        n, m = len(grid), len(grid[0])
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        @cache
        def dp(row, col):
            if not inbound(row, col):
                return float("inf")
            if row == n - 1 and col == m - 1:
                return grid[row][col]
            return min(dp(row + 1, col), dp(row, col + 1)) + grid[row][col]
        return dp(0, 0)