class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = defaultdict(int)  # ratio
        ans = 0
        for w, h in rectangles: # ratio  1/2:4
            r = w / h
            ans += ratio[r]
            ratio[r] += 1
        
        return ans
        