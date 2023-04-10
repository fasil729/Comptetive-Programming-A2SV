class Solution:
    def splitString(self, s: str) -> bool:
        
        n = len(s)
        def helper(start, last):
            if start >= n:
                return True
            val = 0
            for ind in range(start, n):
                val = 10 * val + int(s[ind])
                if val == 0 and ind != n - 1:
                    continue
                if val == last - 1:
                    return helper(ind + 1, val)
                if val > last:
                    return False
                
            return False
        val = 0
        for ind in range(n - 1):
            val = 10 * val + int(s[ind])
            if helper(ind + 1, val):
                return True
        return False
            
    
            
            