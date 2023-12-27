class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        maxi = neededTime[0]
        n = len(colors)
        ans = 0
        
        for ind in range(1, n):
            if colors[ind] != colors[ind - 1]:
                ans += maxi
                maxi = 0
                
            maxi = max(maxi, neededTime[ind])
            
            if ind == n - 1:
                ans += maxi
        
        return sum(neededTime) - ans
                
        
        