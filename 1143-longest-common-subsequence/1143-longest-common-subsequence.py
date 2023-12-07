class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
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
            