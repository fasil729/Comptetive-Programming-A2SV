class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <= 1:
            return x ** n
        mid = n // 2
        if n < 0:
            return self.myPow(1/x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, mid) 
        else:
            return x * self.myPow(x * x, (n - 1) // 2)
        
        