class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def dp(index):
            if index == n - 1:
                return 0
            
            ans = -1
            for ind in range(index + 1, n):
                if abs(nums[ind] - nums[index]) <= target:
                    if dp(ind) == -1:
                        continue
                    ans = max(ans, dp(ind) + 1)
            return ans
        return dp(0)
                    
                    
        