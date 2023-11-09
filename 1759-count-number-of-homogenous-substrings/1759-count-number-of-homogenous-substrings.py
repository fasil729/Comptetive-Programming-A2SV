class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10 ** 9 + 7
        count = 0
        n = len(s)
        ans = 0
        
        for ind in range(n):
            if ind == 0 or s[ind] != s[ind - 1]:
                count = 0
            count += 1
            ans += count
            
        return ans % mod
        