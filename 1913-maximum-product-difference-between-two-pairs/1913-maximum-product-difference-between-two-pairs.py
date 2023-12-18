class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        w, x, y, z = 0, 0, inf, inf
        
        for num in nums:
            if num >= w:
                x = w
                w = num
            elif x < num:
                x = num
                
            if num <= z:
                y = z
                z = num
            elif y > num:
                y = num
                
        return (w * x) - (y * z)
                