class Solution:
    def __init__ (self):
            self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]