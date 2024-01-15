class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        
        @cache
        def dp(ind, countA, countB):
            if countA == countB == n:
                return 0
            
            if countA > n or countB > n:
                return inf
            A, B = costs[ind]
            return min(dp(ind + 1, countA + 1, countB) + A,  dp(ind + 1, countA, countB + 1) + B)
                
            
        return dp(0, 0, 0)
    
    
    def twoCitySchedCost2(self, costs: List[List[int]]) -> int:
        # greedy approach
        n = len(costs)
        
        costs.sort(key=lambda x: x[1] - x[0])
        ans = 0
        for ind, cost in enumerate(costs):
            costA, costB = cost
            if ind < n // 2:
                ans += costB
            else:
                ans += costA
        return ans
            
            
       
        
        
                
                
            
        
        