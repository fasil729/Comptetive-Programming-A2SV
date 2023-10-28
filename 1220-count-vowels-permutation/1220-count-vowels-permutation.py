class Solution:
    def countVowelPermutation1(self, n: int) -> int:
        # top down dp approach
        graph = {}
        mod = 10 ** 9 + 7
        
        graph["a"] = ["e"]
        graph["e"] = ["a", "i"]
        graph["i"] = ["a", "e", "o", "u"]
        graph["o"] = ["i", "u"]
        graph["u"] = ["a"]
        vowels = ["a", "e", "i", "o", "u"]
        
        @cache
        def dp(node, n):
            if n == 1:
                return 1
            ans = 0
            for neigh in graph[node]:
                ans += dp(neigh, n - 1)
            
            return ans % mod
        ans = 0
        for node in vowels:
            ans += dp(node, n)
            
        return ans % mod
    
    def countVowelPermutation(self, n: int) -> int:
        # top down dp approach
        graph = {}
        mod = 10 ** 9 + 7
        
        graph["a"] = ["e"]
        graph["e"] = ["a", "i"]
        graph["i"] = ["a", "e", "o", "u"]
        graph["o"] = ["i", "u"]
        graph["u"] = ["a"]
        vowels = ["a", "e", "i", "o", "u"]
        
        dp = {v:1 for v in vowels}
        
        
        for i in range(2, n + 1):
            prev = dp.copy()
            for node in vowels:
                dp[node] = 0
                for neigh in graph[node]:
                    dp[node] += prev[neigh] 
                
                dp[node] %= mod
        return sum(dp.values()) % mod
                
        
        