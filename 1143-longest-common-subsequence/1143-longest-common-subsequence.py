class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        # top down dp approach
        n = len(text1)
        m = len(text2)
        
        @cache
        def dp(ind1, ind2):
            if ind1 == n or ind2 == m:
                return 0
            
            
            if text1[ind1] == text2[ind2]:
                return dp(ind1 + 1, ind2 + 1) + 1
            
            return max(dp(ind1 + 1, ind2), dp(ind1, ind2 + 1))
        
        return dp(0, 0)
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # bottom up dp approach
        n = len(text1)
        m = len(text2)
        
        prev = [0] * (m + 1)
        
        
        for ind1 in range(n - 1, -1, -1):
            
            dp = [0] * (m + 1)
            for ind2 in range(m - 1, -1, -1):
                if text1[ind1] == text2[ind2]:
                    dp[ind2] = prev[ind2 + 1] + 1
                    
                else:
                    dp[ind2] = max(prev[ind2], dp[ind2 + 1])
            prev = dp
            
        return dp[0]
            
    
    
    
            