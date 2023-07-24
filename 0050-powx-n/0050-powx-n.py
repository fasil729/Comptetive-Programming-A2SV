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
    
    
    def myPow2(self, x: float, n: int) -> float:
        #recursive approach
        if n <= 1:
            return x ** n
        mid = n // 2
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, mid) 
        else:
            return x * self.myPow(x * x, (n - 1) // 2)
        
        