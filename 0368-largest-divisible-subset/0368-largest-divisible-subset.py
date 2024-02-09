class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        
        
        @cache
        def dp(ind):
            if ind == n - 1:
                return [nums[ind]]
            
            num = nums[ind]
            ans = [num]
            temp = []
            for i in range(ind + 1, n):
                if nums[i] % num == 0:
                    temp = [num] + dp(i)
                
                if len(temp) > len(ans):
                    ans = temp
            
            return ans
        
        ans = []
        for i in range(n):
            temp = dp(i)
            if len(temp) > len(ans):
                ans = temp
        
        return ans
    
                
                
            
        