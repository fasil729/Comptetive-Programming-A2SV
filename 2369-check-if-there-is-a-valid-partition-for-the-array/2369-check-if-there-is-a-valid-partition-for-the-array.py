class Solution:
    def validPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        # top down dp approach
        @cache
        def dp(index):
            if index == n:
                return True
            if index < n - 2:
                if nums[index] == nums[index + 1] == nums[index + 2]:
                    return dp(index + 2) or dp(index + 3)
                elif nums[index] + 2 == nums[index + 1] + 1 == nums[index + 2]:
                    return dp(index + 3)
                    
            if index < n - 1 and nums[index] == nums[index + 1]:
                return dp(index + 2)
            return False
        return dp(0)
    
    def validPartition(self, nums: List[int]) -> bool:
        # bottom up dp approach
        n = len(nums)
        dp = {n: True}
        for index in range(n - 1, -1, -1):
            if index not in dp:
                dp[index] = False
            if index < n - 2:
                if nums[index] == nums[index + 1] == nums[index + 2]:
                    dp[index] = dp[index] or dp[index + 3]
                elif nums[index] + 2 == nums[index + 1] + 1 == nums[index + 2]:
                    dp[index] = dp[index] or dp[index + 3]
                    
            if index < n - 1 and nums[index] == nums[index + 1]:
                dp[index] = dp[index] or dp[index + 2]
        
        return dp[0]
            
            
    
       
        