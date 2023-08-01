class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @cache
        def dp(index, half_sum):
            if index == len(nums) or half_sum == 0:
                return half_sum == 0
            if half_sum < 0:
                return False
            
            
            return dp(index + 1, half_sum - nums[index]) or dp(index + 1, half_sum)
        return dp(0,  sum(nums) / 2)
        
        