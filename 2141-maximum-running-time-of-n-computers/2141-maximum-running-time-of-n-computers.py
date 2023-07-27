class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        left, right = 0, sum(batteries)
        
        while left < right:
            print(left, right)
            mid = ((right + left) // 2)+ 1
            if self.is_possible(n, batteries, mid):
                left = mid
            else:
                right = mid - 1
        return left
        
        
    
    
    def is_possible(self, n, batteries, t):
        sum = 0
        for b in batteries:
            sum += b
            if sum >= t:
                sum -= t
                n -= 1
        if n <= 0:
            return True
        return False
    
        
        