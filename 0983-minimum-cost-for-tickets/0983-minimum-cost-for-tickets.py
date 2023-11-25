class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        maxi = max(days)
        
        # top down dp approach
        @cache
        def dp(ind, max_day):
            if ind == n:
                return 0
            day = days[ind]
            ans = inf
            if max_day >= maxi:
                return 0
            if max_day >= day:
                ans = min(ans, dp(ind + 1, max_day))
            return min(ans, dp(ind + 1, day) + costs[0], dp(ind + 1, day + 6) + costs[1], dp(ind + 1, day + 29) + costs[2])
        
        return dp(0, 0)
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        
        
        # bottom up dp approach
        maxi = max(days)
        prev = [0] * (maxi + 1)
       
        n = len(days)
        
        for ind in range(n - 1, -1, -1):
            dp = [inf] * (maxi + 1)
            day = days[ind]
            
            for max_day in range(maxi, -1, -1):
                index = max_day
                if max_day >= day:
                    dp[index] = min(dp[index], prev[index])
                
                new_day = day   
                one =  prev[index] + costs[0]
                
                new_day = min(day + 6, maxi)
                seven =  prev[new_day] + costs[1]
                
                new_day = min(day + 29, maxi)
                thirty =  prev[new_day] + costs[2]
                
                dp[index] = min(dp[index], one, seven, thirty)
            prev = dp
        # print(dp)
        return dp[0]
            
        
        
        
        