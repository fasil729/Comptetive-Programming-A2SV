class Solution:
    def numDistinct1(self, s: str, t: str) -> int:
        # top down dp approach
        n = len(s)
        m = len(t)
        
        @cache
        def dp(ind1, ind2):
            if ind2 == m:
                return 1
            
            if ind1 == n:
                return 0
            
            ans = 0
            if s[ind1] == t[ind2]:
                ans += dp(ind1 + 1, ind2 + 1)
            
            ans += dp(ind1 + 1, ind2)
            
            return ans
        
        return dp(0, 0)
    
    def numDistinct(self, s: str, t: str) -> int:
        # bottom up dp approach
        n = len(s)
        m = len(t)
        
        prev = [0] * m + [1]
        
        for ind1 in range(n - 1, -1, -1):
            dp = [0] * m + [1]
            
            for ind2 in range(m - 1, -1, -1):
                if s[ind1] == t[ind2]:
                    dp[ind2] += prev[ind2 + 1]
                    
                dp[ind2] += prev[ind2]
            
            prev = dp
        
        return dp[0]
                
            
        