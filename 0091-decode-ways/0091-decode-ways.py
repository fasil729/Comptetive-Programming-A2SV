class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        @cache
        def dp(index):
            # print(index, "index")
            if index >= n:
                return 1
            
            ans = 0
            
            if "1" <= s[index] <= "9":
                ans += dp(index + 1)
            
            
            if index != n - 1 and "1" <= s[index:index + 2] <= "26":
                
                ans += dp(index + 2)
            return ans
        
        return dp(0)
            
            
        