class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        pos = 0
        neg = 0
        n = len(nums)
        
        
        while pos < n and neg < n:
           
            while nums[pos] < 0:
                pos += 1
                
            while nums[neg] > 0:
                neg += 1
                
            ans.append(nums[pos])
            ans.append(nums[neg])
            pos += 1
            neg += 1
                
    
        return ans