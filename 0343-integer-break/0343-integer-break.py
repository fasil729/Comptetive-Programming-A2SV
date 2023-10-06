class Solution:
    def integerBreak(self, n: int) -> int:
        
        
        @cache
        def dp(n):
            if n == 1:
                return 1
            ans = 1
            for i in range(1, n):
                ans = max(ans, i * (n - i))
                ans = max(ans, i * dp(n - i))
            return ans
        return dp(n)