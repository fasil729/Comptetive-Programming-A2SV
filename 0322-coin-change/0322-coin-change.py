class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        
        # top down approach
        @cache
        def dp(target):
            if target == 0:
                return 0
           
            ans = inf
            for c in coins:
                if c <= target:
                    ans = min(ans, dp(target - c) + 1)
            return ans
        res =  dp(amount)
        return res if res != inf else -1
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # bottom up approach
        dp = defaultdict(lambda: inf)
        dp[0] = 0
        for n in range(amount + 1):
            for c in coins:
                if c <= n:
                    dp[n] = min(dp[n], dp[n - c] + 1)
        return dp[amount] if dp[amount] != inf else -1
    