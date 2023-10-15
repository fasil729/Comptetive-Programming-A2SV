class Solution:
    def numWays1(self, steps: int, arrLen: int) -> int:
        # top down dp approach
        mod = 10 ** 9 + 7
        
        @cache
        def dp(index, left_step):
            if left_step == 0 and index == 0:
                return 1
            if left_step == 0:
                return 0
            left, stay, right = 0, 0, 0
            if index > 0:
                left = dp(index - 1, left_step - 1)
            if index < arrLen - 1:
                right = dp(index + 1, left_step - 1)
            stay = dp(index, left_step - 1)
            return (left + stay + right) % mod
        
        return dp(0, steps)
    
    def numWays(self, steps: int, arrLen: int) -> int:
        # bottom up dp approach with minimized space complexity
        mod = 10 ** 9 + 7
        arrLen = min(steps + 1, arrLen)
        prev_dp = [0] * arrLen
        prev_dp[0] = 1
        
        for step in range(1, steps + 1):
            dp = []
            for ind in range(0, arrLen):
                
                ans = 0
                if ind > 0:
                    ans += prev_dp[ind - 1]
                if ind < arrLen - 1:
                    ans += prev_dp[ind + 1]
                ans += prev_dp[ind]
                dp.append(ans % mod)
            prev_dp = dp
        return dp[0]
                
                
            
        
        