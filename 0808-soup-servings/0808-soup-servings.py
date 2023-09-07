class Solution:
    def soupServings1(self, n: int) -> float:
        
        
        def dp(soup_a, soup_b):
            if soup_a <= 0 and soup_b <= 0:
                return 0, 0, 1
            
            num_a, num_both, num = 0, 0, 0
            operations = [[100, 0], [75, 25], [50, 50], [25, 75]]
            if soup_a <= 0:
                operations = operations[1:]
            for a, b in operations:
                n_a = soup_a - a
                n_b = soup_b - b
                if n_a <= 0 and n_b <= 0:
                    num_both += 1
                elif n_a <= 0:
                    num_a += 1
                w_a, w_b, w = dp(n_a, n_b)
                num_a += w_a
                num_both += w_b
                num += w_b
            return num_a, num_both, num
        
        ways_a, ways_b, ways = dp(n, n)
        prob = ways_a
        return 0
        
    def soupServings(self, n: int) -> float:
        import sys
        sys.setrecursionlimit(10**6) 
        @cache
        def dp(i, j):
            if i <= 0 and j <= 0:
                return 0.5
            elif i <= 0:
                return 1
            elif j <= 0:
                return 0
            return 0.25 * (dp(i - 4, j) + dp(i - 3, j - 1) + dp(i - 2, j - 2) + dp(i - 1, j - 3))
        m = math.ceil(n/25)
        for k in range(1, m + 1):
            if dp(k, k) > 1 - 1e-5:
                return 1.0
        return dp(m, m)
                
            
        
                
        