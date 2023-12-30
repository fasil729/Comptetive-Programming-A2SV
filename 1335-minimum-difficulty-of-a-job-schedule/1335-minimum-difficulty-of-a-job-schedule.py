class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        n = len(jobDifficulty)
        @cache
        def dp(ind, d):
            if d == 0 and ind == n:
                return 0
            if ind == n or d == 0:
                return inf
            
            res = inf
            maxi = 0
            for j in range(ind, n):
                maxi = max(maxi, jobDifficulty[j])
                res = min(res, dp(j + 1, d - 1) + maxi)
            
            return res
        
        ans = dp(0, d)
        return ans if ans != inf else -1 
    
    def minDifficulty2(self, jobDifficulty: List[int], d: int) -> int:
        
        # bottom up dp approach
        n = len(jobDifficulty)
        days = d
        prev = [0] + [inf] * days
        
        for ind in range(n - 1, -1, -1):
            dp = [inf] * (days + 1) 
            
            for d in range(days + 1):
                
                maxi = 0
                for j in range(ind, n):
                    maxi = max(maxi, jobDifficulty[j])
                    dp[d] = min(dp[d], prev[d - 1] + maxi)
            print(dp)
            prev = dp
        print(dp) 
        return dp[days] if dp[days] != inf else -1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            