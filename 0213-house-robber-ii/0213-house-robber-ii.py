class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(index, first):
            if index >= n:
                return 0
            if index == n - 1 and first:
                return 0
            
            return max(dp(index + 1, first), dp(index + 2, first) + nums[index])
        
        return max(dp(1, False), dp(2, True) + nums[0])
            
        