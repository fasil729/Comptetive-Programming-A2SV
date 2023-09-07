class Solution:
    def minRefuelStops1(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # brute_force
        stations.append([target, 0])
        stations.append([0, 0])
        
        stations.sort()
        @cache
        def dp(prev_fuel, index):
            position, fuel = stations[index]
            prev_fuel -= position - stations[index - 1][0]
            if prev_fuel < 0:
                return -1
            if position == target:
                return 0
            res = inf
            ans = dp(prev_fuel, index + 1)
            if ans != -1:
                res = min(res, ans)
            ans = dp(prev_fuel + fuel, index + 1)
            if ans != -1:
                res = min(res, ans + 1)
            return res if res != inf else -1
        return dp(startFuel, 1)
    
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # dp bottom up
        dp = defaultdict(int)
        dp[0] = startFuel
        for i, (position, fuel) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= position:
                    dp[t + 1] = max(dp[t + 1], dp[t] + fuel)
        for k, dist in sorted(dp.items()):
            if dist >= target:
                return k
        return -1
        
            