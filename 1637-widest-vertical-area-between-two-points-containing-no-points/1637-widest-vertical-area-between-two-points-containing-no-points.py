class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ans = 0
        
        prev = points[0][0]
        for x, y in points:
            ans = max(ans, x - prev)
            prev = x
            
        return ans