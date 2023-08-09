class Solution:
    def __init__ (self):
            self.memo = {}
    def climbStairs1(self, n: int) -> int:
        # top down dp
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
    
    def climbStairs(self, n: int) -> int:
        #bottom up dp
        first, second = 0, 1
        for i in range(1, n + 1):
            third = second + first
            first = second
            second = third
        return third
            
            
            
        
    
    
        