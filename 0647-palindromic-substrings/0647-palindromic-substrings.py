class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        def dp(start, end):
            
            if start < 0 or end == n:
                return 0
            
            if s[start] == s[end]:
                return dp(start - 1, end + 1) + 1
            
            return 0
        
        
        ans = 0
        for ind in range(n):
            ans += dp(ind, ind)
            ans += dp(ind, ind + 1)
            
        return ans
        