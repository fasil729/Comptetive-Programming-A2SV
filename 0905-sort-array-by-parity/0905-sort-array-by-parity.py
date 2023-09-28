class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and not nums[i] % 2:
                i += 1
            while i < j and nums[j] % 2:
                j -= 1
            
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
                
        
        return nums
        