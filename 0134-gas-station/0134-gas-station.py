class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        # greedy approach and find the smallest index with diff > 0
        ans, total = 0, 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                # fail -> reset
                total = 0
                ans = i + 1
        
        return ans



class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            return 0 if gas[0] - cost[0] >= 0 else -1
        res = -1
        tot = 0
        last = -1
        for ind, g in enumerate(gas):
            diff = g - cost[ind]
            tot += diff
           
            prev = gas[ind - 1] - cost[ind - 1]
            if diff > 0 and prev <= 0 and last < 0:
                res = ind
                last = 0
            last += diff
            
            
        return res if tot >= 0 else -1 
            
        
        