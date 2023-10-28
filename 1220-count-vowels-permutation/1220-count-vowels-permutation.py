class Solution:
    def countVowelPermutation(self, n: int) -> int:
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
            
        
        