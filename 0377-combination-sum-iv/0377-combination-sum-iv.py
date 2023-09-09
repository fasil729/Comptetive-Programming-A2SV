class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
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