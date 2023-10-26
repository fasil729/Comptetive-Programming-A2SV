class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # top_down dp approach
        n = len(prices)
        
        @cache
        def dp(index, has_stock):
            if index == n:
                return 0
            price = prices[index]
            if has_stock:
                ans = dp(index + 1, not has_stock) + price - fee
            else:
                ans = dp(index + 1, not has_stock) - price
            return max(ans, dp(index + 1, has_stock))
        return dp(0, False)
    
    def maxProfit2(self, prices: List[int], fee: int) -> int:
        #greedy approach need to fix it
        mini = prices[0]
        res = 0
        for price in prices[1:]:
            if mini < price - fee:
                res += price - mini - fee
                mini = price
            else:
                mini = min(price, mini)
            
        return res
        