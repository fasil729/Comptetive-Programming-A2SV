class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def dp(n):
            if n == 1:
                return 1
            a = 2 * n - 1
            return (a + 1) * a // 2 * dp(n - 1) % mod
        return dp(n)
        