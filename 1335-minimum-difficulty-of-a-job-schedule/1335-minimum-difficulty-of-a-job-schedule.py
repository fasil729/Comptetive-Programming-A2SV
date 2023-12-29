class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        
        
        n = len(jobDifficulty)
        @cache
        def dp(ind, d):
            if d == 0 and ind == n:
                return 0
            if ind == n or d == 0:
                return inf
            
            res = inf
            maxi = 0
            for j in range(ind, n):
                maxi = max(maxi, jobDifficulty[j])
                res = min(res, dp(j + 1, d - 1) + maxi)
            
            return res
        
        ans = dp(0, d)
        return ans if ans != inf else -1 