class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pref = [0]
        tot = sum(nums)
        
        for num in nums:
            pref.append(pref[-1] + num)
    
        n = len(nums)
        ans = []
        for i in range(n):
            left_sum = pref[i]
            right_sum = tot - pref[i + 1] 
            num = nums[i]
            left_diff = (i * num) - left_sum
            right_diff = right_sum - (n - i - 1) * num
            ans.append(left_diff + right_diff)
        
        return ans
            
        
        