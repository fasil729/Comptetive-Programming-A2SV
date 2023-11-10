class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        
        half = sum(nums) / 2
        n = len(nums)
        # top down
        @cache
        def dp(ind, tot):
            if tot == 0:
                return True
            if ind == n or tot < 0:
                return False
            
            return dp(ind + 1, tot) or dp(ind + 1, tot - nums[ind])
        
        return dp(0, half)
            
    
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        half = sum(nums) // 2
        
        n = len(nums)
        # bottom up
        dp = [False for i in range(half + 1)]
        dp[0] = True
        
        for ind in range(n - 1, -1, -1):
            prev = dp.copy()
            
            
            for half_sum in range(half + 1):
                dp[half_sum] = False
                dp[half_sum] = prev[half_sum]
                if half_sum - nums[ind] >= 0:
                    dp[half_sum] = dp[half_sum] or prev[half_sum - nums[ind]]
            
       
        
        return dp[half]
                
    
            