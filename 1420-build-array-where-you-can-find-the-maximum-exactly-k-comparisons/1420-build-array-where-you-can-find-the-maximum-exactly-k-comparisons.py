class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = (10 ** 9) + 7
        
        @cache
        def dp(ind, b, cost):
            if ind == n and cost == k:
                return 1
            if ind == n:
                return 0
            ans = 0
            for i in range(1, m + 1):
                if k == cost and i > b:
                    break
                ans += dp(ind + 1, max(i, b), cost + int(i > b))
                
            return ans % mod
        return dp(0, 0, 0)
                
                
            
            