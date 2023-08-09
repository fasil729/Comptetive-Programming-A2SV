class Solution:
    def numRollsToTarget1(self, n: int, k: int, target: int) -> int:
        # top down dp
        @cache
        def dp(n, target):
            if not n and not target:
                return 1
            if not n:
                return 0
            res = 0
            for j in range(1, k + 1):
                if j <= target:
                    res += dp(n - 1, target - j)
            return res
        return dp(n, target) % (10 ** 9 + 7)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        def get(t, n):
            if (t, n) in dp:
                return dp[(t, n)]
            return 0
        
        # bottom up approach
        dp = {(0, 0):1}
        c = 0
            
        for t in range(1, target + 1):
            for d in range(1, k + 1):
                for c in range(0, n + 1):
                    if not (t, c) in dp:
                        dp[(t, c)] = 0
                    if d <= t and n >= c: 

                        dp[(t, c)] += get(t - d, c - 1)
                    else:
                        break
        return dp[(target, n)] % (10 ** 9 + 7)
            
    
    
    
                
        