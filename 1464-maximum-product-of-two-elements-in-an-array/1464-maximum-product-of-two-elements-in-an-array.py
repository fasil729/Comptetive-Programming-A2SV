class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi, sec_maxi = 0, 0
        
        for num in nums:
            if maxi <= num:
                sec_maxi = maxi
                maxi = num
            elif sec_maxi < num < maxi :
                sec_maxi = num
            
                
        return (maxi - 1) * (sec_maxi - 1)
        