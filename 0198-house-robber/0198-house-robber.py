class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        @cache
        def dp(ind):
            # top down dp approach
            if ind >= n:
                return 0
            
            
            return max(dp(ind + 2) + nums[ind], dp(ind + 1))
        
        return dp(0)
        