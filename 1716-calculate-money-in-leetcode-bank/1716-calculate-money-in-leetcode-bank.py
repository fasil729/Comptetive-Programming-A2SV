class Solution:
    def totalMoney(self, n: int) -> int:
        
        def weekbank(week, interval):
            return interval * (week + ((interval - 1) / 2))
        
        week = 1
        ans = 0
        
        while n >= 7:
            n -= 7
            ans += int(weekbank(week, 7))
            week += 1
        
        return ans + int(weekbank(week, n))