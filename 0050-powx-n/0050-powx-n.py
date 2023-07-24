class Solution:
    def myPow(self, x: float, n: int) -> float:
        # iterative approach
        if n == 0:
            return 1
        
        exp = abs(n)
        res = x
        rem = 1
        while exp > 1:
            
            if exp % 2:
                rem *= res
            res *= res
            exp //= 2
        res = res * rem   
        if n < 0:
            res = 1 / res
        return res
        
        
        