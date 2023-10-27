class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        @cache
        def dp(start, end):
            if start == end:
                return 1
            if start > end:
                return 0
            
            if s[start] == s[end]:
                return dp(start + 1, end - 1) + 2
            return max(dp(start + 1, end), dp(start, end - 1))
        
        return dp(0, n - 1)
        
        