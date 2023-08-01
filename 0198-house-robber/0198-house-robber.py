class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache
        def dp(index):
            if index >= len(nums):
                return 0
            maxi = 0
            for i in range(index + 2, len(nums)):
                maxi = max(maxi, dp(i))
            
            
            return nums[index] + maxi
        
        return max(dp(0), dp(1))
        
        