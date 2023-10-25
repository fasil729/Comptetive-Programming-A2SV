class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        memo = {}
        def dp(needs):
            if sum(needs) == 0:
                return 0
            s = str(needs)
            if s in memo:
                return memo[s]
            
            ans = 0
            for i in range(n):
                ans += price[i] * needs[i]
            
            for spec in special:
                breaked = False
                new_need = [0] * n
                for i in range(n):
                    cur = needs[i] - spec[i]
                    if cur < 0:
                        breaked = True
                        break
                    new_need[i] = cur
                if breaked:
                    continue
                p = spec[n]
                ans = min(ans, dp(new_need) + p)
            memo[s] = ans
            return ans
        return dp(needs)
                    
        