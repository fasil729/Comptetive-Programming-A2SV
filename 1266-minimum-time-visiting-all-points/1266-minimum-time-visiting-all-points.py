class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        ans = 0
        n = len(points)
        
        for ind in range(1, n):
            x, y = points[ind]
            p_x, p_y = points[ind - 1]
            
            ans += max(abs(p_x - x), abs(p_y - y))
            
        
        return ans
            
        