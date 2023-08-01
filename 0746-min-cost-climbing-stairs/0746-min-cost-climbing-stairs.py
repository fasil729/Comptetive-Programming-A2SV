class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        @cache
        def dp(index):
            if index >= n:
                return 0
            
            
            return cost[index] + min(dp(index + 1), dp(index + 2))
        return min(dp(0), dp(1))
            
            
        