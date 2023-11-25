class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @cache
        def dp(ind, max_day):
            if ind == n:
                return 0
            day = days[ind]
            ans = inf
            if max_day >= 365:
                return 0
            if max_day >= day:
                ans = min(ans, dp(ind + 1, max_day))
            return min(ans, dp(ind + 1, day) + costs[0], dp(ind + 1, day + 6) + costs[1], dp(ind + 1, day + 29) + costs[2])
        
        return dp(0, 0)
        