class Solution:
    def longestPalindrome1(self, s: str) -> str:
        # top down dp
        n = len(s)
        @cache
        def dp(start, end):
            if start >= end:
                return True
            if s[start] == s[end]:
                return dp(start + 1, end - 1)
            return False
        start, end = 0, 0
        for i in range(n):  
            for j in range(n - 1, i, -1):
                diff = end - start
                if dp(i, j):
                    start = i
                    end = j
        ans = s[start:end + 1]
        return ans
    
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]
                    
                    
        
        