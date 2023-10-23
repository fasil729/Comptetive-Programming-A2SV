class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        while k > 0:
            steps = self.getsteps(n, curr, curr + 1) # 0  10
            if steps <= k:
                k -= steps
                curr += 1
            else:
                curr *= 10
                k -= 1
        
        return curr
                
                
        
        
        
    def getsteps(self, n, num1, num2):
        steps = 0
        while num1 <= n:
            steps += min(n + 1, num2) - num1
            num1 *= 10
            num2 *= 10
        return steps
            
        
        