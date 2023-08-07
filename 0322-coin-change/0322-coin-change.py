class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
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