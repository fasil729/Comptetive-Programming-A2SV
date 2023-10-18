class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(ind, target):
            if ind == n and target == 0:
                return 1
            if ind == n:
                return 0
            num = nums[ind]
            return dp(ind + 1, target - num) + dp(ind + 1, target + num)
        
        return dp(0, target)
        