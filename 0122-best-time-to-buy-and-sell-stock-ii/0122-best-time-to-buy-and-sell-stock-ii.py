class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        res = 0
        for price in prices:
            mini = min(price, mini)
            if price > mini:
                res += price - mini
                mini = price
        
        return res
            
        
        