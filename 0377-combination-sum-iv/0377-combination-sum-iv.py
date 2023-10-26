class Solution:
    def combinationSum41(self, nums: List[int], target: int) -> int:
        # top down dp
        @cache
        def dp(target):
            ans = 0
            for num in nums:
                if target - num == 0:
                    ans += 1
                if target - num > 0:
                    ans += dp(target - num)
            return ans
        
        return dp(target)
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # bottom up dp
        dp = {0:1}
        
        for t in range(1, target + 1):
            dp[t] = 0
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]
        return dp[target]
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        