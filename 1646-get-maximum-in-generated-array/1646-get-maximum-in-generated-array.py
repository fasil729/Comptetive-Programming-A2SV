class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        maxi = 0
        @cache
        def dp(n):
            nonlocal maxi
            
            if n <= 1:
                result = n
            elif n % 2:
                result = dp(n // 2) + dp((n // 2) + 1)
            else:
                result = dp(n // 2)
            maxi = max(maxi, result)
            return result
        
        for i in range(n + 1):
            dp(i)
        return maxi