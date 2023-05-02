class Solution:
    @cache
    def myPow(self, x: float, n: int) -> float:
        if n <= 1:
            return x ** n
        mid = n // 2
        return self.myPow(x, mid) * self.myPow(x, n - mid)
        