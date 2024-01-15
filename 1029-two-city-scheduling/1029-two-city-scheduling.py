class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        """
        # intalization
        ans = 0
        Net = []
        n = len(costs) // 2
        
        
        # construct net array
        for ind, cost in enumerate(costs):
            costa, costb = cost
            Net.append((costa - costb, ind))
        
        # sort in ascending order
        Net.sort()
        
        # compute cost
        for i, net in enumerate(Net):
            ind = net[1]
            if i < n:
                ans += costs[ind][0]
            else:
                ans += costs[ind][1]
        
        return ans
        
        
            
            
       
        
        
                
                
            
        
        