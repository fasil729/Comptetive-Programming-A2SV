class Solution:
    def numFactoredBinaryTrees1(self, arr: List[int]) -> int:
        # top down dp
        arr = set(arr)
        mod = 10 ** 9 + 7
        @cache
        def dp(root):  
            ans = 1     
            
            for child in arr:  
                div = int(root/child)  
                if root % child == 0 and div in arr:  
                    ans += dp(child) * dp(div)
            return ans % mod  # 2
        ans = 0
        for root in arr:
            ans += dp(root)
            
        
        return ans % mod
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # bottom up dp
        n = len(arr)
        mod = 10 ** 9 + 7
        arr.sort(reverse=True)
        
        dp = {}
        
        for i in range(n - 1, -1, -1):
            dp[arr[i]] = 1
            for j in range(i + 1, n):
                div = int(arr[i] / arr[j])
                if arr[i] % arr[j] == 0 and div in dp:
                    dp[arr[i]] += dp[arr[j]] * dp[div]
                    
        ans = 0
        for val in dp.values():
            ans += val 
            
        return ans % mod
        
    
                    
        