class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def recursion(a, b):
            if b == 1: 
                return a
            if b == 0:
                return 1
            
            if b % 2 == 0:
                ans = recursion(a, b // 2)
                return ans * ans % mod
            else:
                ans = recursion(a, (b - 1) // 2)
                return a * ans * ans % mod
            
        power, mod = n // 2, 10 ** 9 + 7
        if n % 2 == 0:
            return recursion(20, power) % mod
        else:
            return recursion(5, power + 1) * recursion(4, power) % mod 