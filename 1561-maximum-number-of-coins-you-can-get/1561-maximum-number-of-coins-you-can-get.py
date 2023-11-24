class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        n = len(piles) // 3
        ans = 0
        ind = 1
        while n:
            ans += piles[ind]
            ind += 2
            n -= 1
        
        return ans
            
        
        
        