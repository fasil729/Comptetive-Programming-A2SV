class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        n = len(s)
        def getLength(freq):
            if freq == 1:
                return 1
            return len(str(freq)) + 1
        
        @cache
        def dp(ind, k):
            if k < 0:
                return n
            if ind == n:
                return 0
            
            ans = dp(ind + 1, k - 1)
            freq = 0
            for i in range(ind, n):
                if s[i] == s[ind]:
                    freq += 1
                elif k == 0:
                    return ans
                else:
                    k -= 1
                
                ans = min(ans, dp(i + 1, k) + getLength(freq))
            
            return ans
        
        return dp(0, k)
            
            
        
        
        
            
        