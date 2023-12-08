class Solution:
    def numDistinct(self, s: str, t: str) -> int:
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
            
        