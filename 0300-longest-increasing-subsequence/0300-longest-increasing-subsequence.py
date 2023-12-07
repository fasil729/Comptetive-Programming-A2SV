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
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the first element >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)
    
        