class Solution:
    def rob1(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        @cache
        def dp(ind):
            # top down dp approach
            if ind >= n:
                return 0
            
            
            return max(dp(ind + 2) + nums[ind], dp(ind + 1))
        
        return dp(0)
    def rob(self, nums: List[int]) -> int:
        # bottom up dp approach
        
        n = len(nums)
        first, second = 0, 0
        
        for ind in range(n - 1, -1, -1):
            ans = max(second + nums[ind], first)
            second = first
            first = ans
            
        
        return ans
    
        