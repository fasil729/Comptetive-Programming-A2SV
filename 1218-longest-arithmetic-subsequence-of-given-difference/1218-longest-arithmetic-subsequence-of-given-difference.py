class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        
        # bottom up dp approach
        dp = {}
        maxi = 1
        for i in arr:
            if i - difference not in dp:
                dp[i] = 1
            else:
                dp[i] = 1 + dp[i - difference]
            maxi = max(maxi, dp[i])
        
        return maxi

        
        