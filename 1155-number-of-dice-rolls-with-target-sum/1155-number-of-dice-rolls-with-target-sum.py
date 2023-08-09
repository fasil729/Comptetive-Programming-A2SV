class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
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
                
        