class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(index):
            if index == n - 1:
                return 1
            
            ans = 0
            for i in range(index + 1, n):
                if nums[i] > nums[index]:
                    ans = max(ans, dp(i))
                    
            return ans + 1
        
        res = 0
        for i in range(n):
            res = max(res, dp(i))
        return res
    # def lengthOfLIS1(self, nums: List[int]) -> int:
    #     #binary search
    
        