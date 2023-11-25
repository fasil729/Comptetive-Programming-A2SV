class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = 0
        tot = sum(nums)
        
       
    
        n = len(nums)
        ans = []
        for i in range(n):
            left_sum = pref
            right_sum = tot - pref
            num = nums[i]
            
            left_diff = (i * num) - left_sum
            right_diff = right_sum - (n - i) * num
            
            pref += num
            ans.append(left_diff + right_diff)
            
        return ans
            
        
        