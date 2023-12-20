class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mini, sec_mini = inf, inf
        
        for price in prices:
            if price < mini:
                sec_mini = mini
                mini = price
            else:
                sec_mini = min(price, sec_mini)
                
        total = mini + sec_mini
        if total <= money:
            return money - total
        return money
        