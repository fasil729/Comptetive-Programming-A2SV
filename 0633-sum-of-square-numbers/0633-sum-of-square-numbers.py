class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Two pointer
        left = 0
        right = int(c**0.5)
        
        while left <= right:
            target = left**2 + right**2
            if target == c:
                return True
            if target < c:
                left += 1
            else:
                right -= 1
                
        return False
            
            