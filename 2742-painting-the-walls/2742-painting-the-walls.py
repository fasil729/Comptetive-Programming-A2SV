class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        tot = sum(cost)
        pref_sum = [0]
        for t in time[::-1]:
            pref_sum.append(pref_sum[-1] + t)
        pref_sum = pref_sum[::-1]
        @cache
        def dp(ind, remain):
            if remain <= 0:
                return 0
            if ind == n:
                return tot
            
            return min(dp(ind + 1, remain), dp(ind + 1, remain - time[ind] - 1) + cost[ind])
        
        return dp(0, n)