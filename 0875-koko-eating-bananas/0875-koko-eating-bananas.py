class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        def is_valid(k):
            min_h = 0
            for pile in piles:
                min_h += ceil(pile/k)
            return min_h <= h
        
        
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1
        return left
            
        
        
        
        