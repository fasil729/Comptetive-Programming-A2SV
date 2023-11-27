class Solution:
    def knightDialer(self, n: int) -> int:
        neighbours = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], 
                      [], [0, 1, 7], [2, 6], [1, 3], [2, 4] 
                     ]
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(key, jumps):
            if jumps == 0:
                return 1
            ans = 0
            for neigh in neighbours[key]:
                ans += dp(neigh, jumps - 1)
            
            return ans 
       
        ans = 0
        for key in range(10):
            ans += dp(key, n - 1) 
            
        return ans % MOD
        
        