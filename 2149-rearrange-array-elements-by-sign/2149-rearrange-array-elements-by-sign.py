class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        ans = []
        pos = []
        neg = []
        n = len(nums)
        
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
                
        for ind in range(len(pos)):
            ans.append(pos[ind])
            ans.append(neg[ind])
            
        return ans