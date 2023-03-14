class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000000007
        cof = n / 2
        if n == 1:
            return 5
        if n == 2:
            return 20
        if n % 2:
                return 5 * self.countGoodNumbers(n - 1) % mod
       
        if cof % 2 == 0:
            ans = self.countGoodNumbers(n // 2)
            return ans * ans % mod
        else:
            ans = self.countGoodNumbers((n-1) // 2)
            return 20 * ans * ans % mod
            