class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        
        @cache
        def dp(ind):
            if ind == n - 1:
                return 1
            
            if nums[ind] + 1 == nums[ind + 1]:
                return dp(ind + 1) + 1
            return 1
        
        ans = 0
        for i in range(n):
            ans = max(ans, dp(i))
        
        return ans
        
        
            
        