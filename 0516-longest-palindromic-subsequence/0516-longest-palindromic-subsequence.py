class Solution:
    def longestPalindromeSubseq1(self, s: str) -> int:
        # top down dp approach
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
    
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        dp = [1] * n
        for start in range(n - 1, -1, -1):
            prev = dp.copy()
            for end in range(start + 1, n):
                if s[start]  == s[end]:
                    dp[end] = 2
                    if start + 1 != end:
                        dp[end] += prev[end - 1] 
                else:
                    dp[end] = max(prev[end], dp[end - 1])
       
        return dp[-1]
    def longestPalindromeSubseq2(self, s: str) -> int:
            n = len(s)
            dp = [1] * n
            for end in range(1, n):
                    pre = dp[end]
                    for i in range(end-1, -1, -1):
                        tmp = dp[i]
                        if s[i] == s[end]:
                            dp[i] = 2 + pre if i + 1 <= end - 1 else 2
                        else:
                            dp[i] = max(dp[i + 1], dp[i])
                        pre = tmp
            return dp[0]

    
        