class Solution:
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        
        # top down dp approach
        @lru_cache
        def dp(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]
            
            return triangle[row][col] + min(dp(row + 1, col), dp(row + 1, col + 1))
        
        return dp(0, 0)
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # bottom up dp approach
        prev_dp = triangle[-1]
        m = len(triangle) - 2
        for row in range(m, -1, -1):
            dp = []
            for col in range(row + 1):
                dp.append(min(prev_dp[col], prev_dp[col + 1]) + triangle[row][col])
            prev_dp = dp
        
        return prev_dp[0]
            