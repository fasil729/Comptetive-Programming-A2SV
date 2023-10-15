class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
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
        