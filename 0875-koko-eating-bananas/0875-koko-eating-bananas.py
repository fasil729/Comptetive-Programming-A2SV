class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def getHours(piles, k):
            hr = 0
            for i in piles:
                hr += ceil(i / k)
           
            return hr
        low = 1
        high = max(piles)
        while low <= high:
            mid = low + (high - low) // 2
            if getHours(piles, mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
        