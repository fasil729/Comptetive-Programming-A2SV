class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = defaultdict(int)  # ratio 
        for w, h in rectangles: # ratio  1/2:4
            r = w / h
            ratio[r] += 1
        ans = 0
        for val in ratio.values():
            ans += (val * (val - 1)) // 2
        return ans
        